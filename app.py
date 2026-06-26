import streamlit as st
from agents import run_pipeline

# Page config
st.set_page_config(
    page_title="Multi-Agent Research Assistant",
    page_icon="🤖",
    layout="wide"
)

# Header
st.title("🤖 Multi-Agent Research Assistant")
st.markdown("*Powered by 3 AI agents working together: Researcher → Analyst → Writer*")
st.divider()

# Input
query = st.text_input(
    "Enter your research question:",
    placeholder="e.g. What are the latest breakthroughs in quantum computing in 2025?",
    help="Ask anything — the agents will search the web and produce a full report"
)

col1, col2, col3 = st.columns([1, 1, 4])
with col1:
    run_button = st.button("🚀 Run Research", type="primary")

# Run pipeline
if run_button and query:
    
    with st.spinner("Agents are working... this takes 20-40 seconds"):
        try:
            results = run_pipeline(query)
            
            # Show agent outputs in tabs
            tab1, tab2, tab3 = st.tabs([
                "📋 Final Report", 
                "🔍 Raw Research", 
                "🧠 Analysis"
            ])
            
            with tab1:
                st.markdown("### 📋 Final Report")
                st.markdown(results["final_report"])
                
                # Download button
                st.download_button(
                    label="⬇️ Download Report",
                    data=results["final_report"],
                    file_name="research_report.md",
                    mime="text/markdown"
                )
            
            with tab2:
                st.markdown("### 🔍 Researcher Agent Output")
                st.markdown(results["research"])
            
            with tab3:
                st.markdown("### 🧠 Analyst Agent Output")
                st.markdown(results["analysis"])
                
        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")
            st.info("Check that your API keys in .env are correct")

elif run_button and not query:
    st.warning("Please enter a question first!")

# Sidebar info
with st.sidebar:
    st.markdown("### 🏗️ How it works")
    st.markdown("""
    **Agent 1 — Researcher 🔍**  
    Searches the web using Tavily and extracts key facts
    
    **Agent 2 — Analyst 🧠**  
    Reviews research, finds patterns and gaps
    
    **Agent 3 — Writer ✍️**  
    Produces a clean, professional report
    """)
    st.divider()
    st.markdown("Built with LangChain + Gemini + Tavily")