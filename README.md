# AI Report Generator Agent

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)

## Project Description

The AI Report Generator Agent is an advanced Streamlit-based application designed to automate the creation of comprehensive technical reports. Leveraging powerful AI models and APIs, this tool generates well-structured, insightful reports from a user-provided topic by performing intelligent query generation, web search, and content synthesis.

## Features

- **Automated Query Generation**: Generates diverse and relevant search queries based on the input topic.
- **Asynchronous Web Search**: Performs concurrent web searches using the Tavily API to gather up-to-date information.
- **AI-Powered Report Generation**: Synthesizes search results into a concise, well-organized report with sections including introduction, real-world applications, and industry case studies.
- **Markdown to DOCX Conversion**: Converts the generated markdown report into a downloadable DOCX file.
- **Multi-Model Support**: Supports ChatGroq LLaMA-70B and OpenAI GPT-4o models for flexible report generation.
- **User-Friendly Interface**: Streamlit-based UI with API key management, model selection, and report download functionality.

## Installation

### Prerequisites

- Python 3.9 or higher
- Pandoc (required for markdown to DOCX conversion)
- API keys for:
  - Tavily
  - Groq
  - OpenAI

### Setup Steps

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd report-agent
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install Pandoc:**

   Download and install Pandoc from [https://pandoc.org/installing.html](https://pandoc.org/installing.html).

## Usage

1. **Run the Streamlit app:**

   ```bash
   streamlit run src/agents.py
   ```

2. **Configure API keys:**

   Enter your Tavily, Groq, and OpenAI API keys in the sidebar input fields and click "Submit".

3. **Select the AI model:**

   Choose from available models including ChatGroq LLaMA-70B and OpenAI GPT-4o.

4. **Enter the report topic:**

   Input the topic you want the report to be generated on.

5. **Generate and download the report:**

   Click "Submit" to start the report generation process. Once complete, view the report in the app and download it as a DOCX file.

## Project Structure

```
report-agent/
│
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── src/
│   ├── agents.py             # Core agent logic and Streamlit app
│   ├── state.py              # Data models for agent state and queries
│   ├── prompts.py            # Prompt templates for query and report generation
│   ├── utils.py              # Utility functions (if any)
│   ├── __init__.py           # Package initialization
│   ├── AI.png                # Project image asset
│   ├── logo.jpg              # Project logo
│   ├── output.docx           # Generated report output (example)
│   └── report.md             # Generated markdown report (example)
└── .gitignore
```

## Technologies Used

- [Streamlit](https://streamlit.io/) - Web app framework for Python
- [Langchain](https://github.com/hwchase17/langchain) - Framework for building LLM applications
- [Tavily API](https://tavily.com/) - Web search API for gathering information
- [Groq](https://groq.com/) - AI model provider
- [OpenAI](https://openai.com/) - GPT models for natural language processing
- [Pydantic](https://pydantic.dev/) - Data validation and settings management
- [Pandoc](https://pandoc.org/) - Document converter for markdown to DOCX

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Contact

For questions or support, please contact the project maintainer.
