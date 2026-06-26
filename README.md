# 🤖 Multi-Agent Research Assistant

An AI-powered research assistant that uses **3 specialized agents** working in sequence to search the web, analyze information, and produce structured research reports.

## 🏗️ Architecture
User Query → [Researcher Agent] → [Analyst Agent] → [Writer Agent] → Final Report

- **Researcher Agent** — Searches the web using Tavily and extracts key facts from live sources
- **Analyst Agent** — Reviews research, identifies patterns, gaps, and adds critical thinking
- **Writer Agent** — Synthesizes everything into a clean, structured professional report

## 🛠️ Tech Stack

- **LLM:** LLaMA 3.3 70B via Groq API
- **Agent Framework:** LangChain
- **Web Search:** Tavily Search API
- **Frontend:** Streamlit
- **Language:** Python

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/Suhaani-19/multi-agent-research-assistant.git
cd multi-agent-research-assistant
```

### 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install langgraph langchain langchain-google-genai langchain-community tavily-python python-dotenv streamlit langchain-groq
```

### 4. Set up API keys
Create a `.env` file in the root directory:

GROQ_API_KEY=your_groq_api_key

TAVILY_API_KEY=your_tavily_api_key

Get your free API keys:
- Groq: https://console.groq.com
- Tavily: https://app.tavily.com

### 5. Run the app
```bash
streamlit run app.py
```

## 💡 Example Queries

- *"What are the latest breakthroughs in quantum computing in 2025?"*
- *"What is the current state of AI regulation globally?"*
- *"Compare LangChain vs LlamaIndex for building RAG pipelines"*

## 📁 Project Structure
multi-agent-research/

├── agents.py      # All 3 agent definitions and pipeline logic

├── app.py         # Streamlit UI

├── .env           # API keys (not committed)

└── README.md

