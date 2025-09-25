# Multi-Agent Financial Analysis with CrewAI

# Overview

This repository implements a multi-agent system for financial stock analysis using the CrewAI framework. The system features four specialized AI agents—Data Analyst, Trading Strategy Developer, Trade Advisor, and Risk Advisor—that collaborate to monitor market data, develop trading strategies, plan executions, and assess risks. Originally inspired by a Jupyter notebook tutorial, this project is adapted for a modular Python structure in VS Code and runs locally using Ollama for LLM inference, ensuring no API rate limits.

The agents use tools for web scraping and search to gather real-time data on stocks like Wipro (WIPRO.NS). The workflow follows a hierarchical process managed by an LLM, producing comprehensive reports on trends, strategies, and risks.

## Features

- **Multi-Agent Collaboration**: Agents delegate tasks and share insights for end-to-end analysis.
- **Local LLM Inference**: Powered by Ollama (e.g., DeepSeek-R1:7b model) for privacy and unlimited usage.
- **Modular Design**: Separated into config, agents, tasks, and crew modules for easy maintenance.
- **Tools Integration**: Supports SerperDevTool for search and ScrapeWebsiteTool for content extraction.
- **Customizable Inputs**: Adjust stock selection, risk tolerance, and trading preferences via `main.py`.

## Prerequisites

- Python 3.10+
- Ollama installed and running (with a model like `deepseek-r1:7b` pulled).
- Git for version control.

## Installation

1. **Clone the Repository**:
   ```
   git clone https://github.com/your-username/financial-crewai.git
   cd financial-crewai
   ```

2. **Set Up Virtual Environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```
   pip install crewai crewai_tools langchain-ollama python-dotenv
   ```

4. **Configure Environment**:
   - Create `.env` file in the root directory.
   - Add your Serper API key (free tier available at serper.dev):
     ```
     SERPER_API_KEY=your_serper_key_here
     ```

5. **Start Ollama**:
   - Ensure Ollama is running: `ollama serve`.
   - Pull the model: `ollama pull deepseek-r1:7b` (or your preferred model).

## Usage

1. **Run the Analysis**:
   ```
   python main.py
   ```
   - This kicks off the crew with default inputs (e.g., stock: 'Wipro', risk: 'Medium', preference: 'Day Trading').
   - Output: A detailed report printed to console, including insights, strategies, execution plans, and risk assessment.

2. **Customize Inputs**:
   - Edit `main.py` to modify `financial_trading_inputs` (e.g., change stock to 'AAPL').

3. **Monitor Output**:
   - Agents will use tools to fetch data and collaborate. Local models may take time for inference (1-2 minutes per task on CPU).

## Project Structure

```
financial-crewai/
├── src/
│   ├── config.py          # LLM and environment setup
│   ├── agents.py          # Agent definitions
│   ├── tasks.py           # Task definitions
│   └── crew.py            # Crew assembly
├── main.py                # Entry point
├── .env                   # API keys (gitignore'd)
├── .gitignore
└── requirements.txt       # Dependencies
```

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request with a clear description of changes.

