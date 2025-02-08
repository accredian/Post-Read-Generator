# AI Report Generator Agent

## Overview

The AI Report Generator Agent is a cutting-edge Streamlit application designed to streamline the process of generating comprehensive technical reports. By leveraging the power of advanced AI models and APIs, this app empowers users to produce well-structured reports effortlessly.

## Features

- **Query Generation**: Automatically generate search queries based on the provided topic.
- **Web Search**: Perform web searches to gather relevant information.
- **Report Generation**: Create a concise and comprehensive report using the gathered information.
- **Markdown to DOCX Conversion**: Convert the generated markdown report to a DOCX file.

## Installation

### Prerequisites

- Python 3.9 or higher
- Streamlit
- langgraph
- Pandoc (for markdown to DOCX conversion)
- Required Python packages (listed in `requirements.txt`)

### Steps

1. **Clone the Repository**:
   `git clone repo`
   `cd report agent`
2. **Create a Virtual Environment**:
    `python -m venv myenv`
    `source myenv/bin/activate`
    *On Windows use*: `.\myenv\Scripts\activate`

3. **Install Dependencies**:
    `pip install -r requirements.txt`

### Usage

1. **Run the Streamlit App**:
`streamlit run app.py`

2. **Enter API Keys**:
    - Enter your Tavily, Groq, and OpenAI API keys in the sidebar and click "Save API Keys".

3. **Select Model**:
    - Choose between "ChatGroq LLaMA-70B" and "OpenAI GPT-4o" in the sidebar.

4. **Generate Report**:
    - Enter the topic for the report and click "Submit".
    - The app will generate a report and provide options to download it as a DOCX file.

### Example

    - Here’s an example of how to use the app:

    - Run the app using streamlit run app.py.

    - Enter your API keys and save them.

    - Select the desired model.

    - Enter the topic "Artificial Intelligence in Healthcare".

    - Click "Submit" to generate the report.

    - Download the generated report as a DOCX file.
    