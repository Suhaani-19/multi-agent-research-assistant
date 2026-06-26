from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the LLM (Groq - free & very fast)
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3
)

# Initialize web search tool
search_tool = TavilySearchResults(
    max_results=5,
    tavily_api_key=os.getenv("TAVILY_API_KEY")
)

def researcher_agent(query: str) -> str:
    """Agent 1: Searches the web and gathers raw information"""
    
    print("🔍 Researcher Agent working...")
    
    # Search the web
    search_results = search_tool.invoke(query)
    
    # Format results
    raw_info = ""
    for i, result in enumerate(search_results, 1):
        raw_info += f"\nSource {i}: {result['url']}\n{result['content']}\n"
    
    # Ask LLM to organize the raw search data
    messages = [
        SystemMessage(content="""You are a Research Agent. Your job is to:
1. Read raw search results carefully
2. Extract the most important facts, data, and insights
3. Organize them clearly with bullet points
4. Note which sources support which facts
Be thorough and factual. Do not add opinions."""),
        HumanMessage(content=f"Query: {query}\n\nRaw search results:\n{raw_info}\n\nExtract and organize the key information:")
    ]
    
    response = llm.invoke(messages)
    return response.content


def analyst_agent(query: str, research: str) -> str:
    """Agent 2: Analyzes the research, finds gaps, adds critical thinking"""
    
    print("🧠 Analyst Agent working...")
    
    messages = [
        SystemMessage(content="""You are a Critical Analyst Agent. Your job is to:
1. Review the research provided
2. Identify the most important insights and patterns
3. Point out any gaps, contradictions, or limitations
4. Add context and deeper analysis
5. Highlight what is well-supported vs uncertain
Be analytical, objective, and structured."""),
        HumanMessage(content=f"Original Query: {query}\n\nResearch gathered:\n{research}\n\nProvide your critical analysis:")
    ]
    
    response = llm.invoke(messages)
    return response.content


def writer_agent(query: str, research: str, analysis: str) -> str:
    """Agent 3: Takes research + analysis and writes a clean final report"""
    
    print("✍️ Writer Agent working...")
    
    messages = [
        SystemMessage(content="""You are a Professional Writer Agent. Your job is to:
1. Take the research and analysis provided
2. Write a clear, well-structured report that directly answers the query
3. Use this format:
   - ## Executive Summary (2-3 sentences)
   - ## Key Findings (bullet points)
   - ## Detailed Analysis (paragraphs)
   - ## Conclusion
4. Make it readable, professional, and insightful
5. Do not make up information - only use what was provided"""),
        HumanMessage(content=f"Query: {query}\n\nResearch:\n{research}\n\nAnalysis:\n{analysis}\n\nWrite the final report:")
    ]
    
    response = llm.invoke(messages)
    return response.content


def run_pipeline(query: str) -> dict:
    """Runs all 3 agents in sequence and returns all outputs"""
    
    print(f"\n🚀 Starting Multi-Agent Research Pipeline")
    print(f"📌 Query: {query}\n")
    
    # Agent 1: Research
    research = researcher_agent(query)
    
    # Agent 2: Analysis  
    analysis = analyst_agent(query, research)
    
    # Agent 3: Write final report
    final_report = writer_agent(query, research, analysis)
    
    print("\n✅ Pipeline complete!")
    
    return {
        "query": query,
        "research": research,
        "analysis": analysis,
        "final_report": final_report
    }