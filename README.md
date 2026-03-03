# PS_Level1_Atlassian_MCP
Use an MCP (Model Context Protocol) client of your choice to connect with the Atlassian Remote MCP integration. Your goal is to retrieve and analyze bug data to identify overall trends and categorize the root causes of defects that were missed during development.


# Jira MCP Assessment

A repository for connecting to Atlassian's Model Context Protocol (MCP) and analyzing Jira bug data.

## Overview

This project demonstrates how to connect to the Atlassian Remote MCP server, retrieve bug data from Jira, and perform analysis on root causes, trends, and resolution metrics.

## Prerequisites

- Python 3.x
- Atlassian API Token (generated from [Atlassian Account Settings](https://id.atlassian.com/manage-profile/security/api-tokens))
- Access to a Jira instance

## Setup

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd jira_mcp_asses
   ```

2. Create a virtual environment:
   ```bash
   python -m venv mcp-env
   ```

3. Activate the virtual environment:
   - **Windows (PowerShell):**
     ```powershell
     .\mcp-env\Scripts\Activate.ps1
     ```
   - **Windows (Command Prompt):**
     ```cmd
     mcp-env\Scripts\activate.bat
     ```
   - **Linux/Mac:**
     ```bash
     source mcp-env/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install requests python-dotenv pandas matplotlib
   ```

5. Configure environment variables by creating a `.env` file:
   ```env
   ATLASSIAN_EMAIL=your-email@example.com
   ATLASSIAN_API_TOKEN=your-api-token
   MCP_URL=https://mcp.atlassian.com/v1/sse
   JIRA_URL=https://your-instance.atlassian.net
   PROJECT_KEY=YOUR_PROJECT_KEY
   ```

## Usage

### Connection Check

Test your MCP connection:

```bash
python connection_check.py
```

### Jupyter Notebook Analysis

Open the notebook to perform detailed analysis:

```bash
jupyter notebook "Level1 Attlasian MCP.ipynb"
```

The notebook includes:

1. **Connect to Atlassian Remote MCP** - Establish connection using Python SDK
2. **Retrieve Bug Data** - Fetch bugs from specified Jira project
3. **Analyze Trends** - Weekly/monthly bug creation, open vs closed status
4. **Categorize Root Causes** - Classify bugs into categories:
   - Coding Defects
   - Design / Architecture Issues
   - Process / Tooling Issues
   - Requirement Gaps
   - Testing Gaps
   - Human Factors
5. **Present Findings** - Visualizations and metrics

## Key Metrics Analyzed

- **Total Bugs** - Count of all bug issues
- **MTTR (Mean Time to Resolve)** - Average resolution time in days
- **Severity Distribution** - Breakdown by priority (Critical, High, Normal, Low)
- **Component Distribution** - Bugs by team/module
- **Root Cause Distribution** - Categorization of documented root causes

## Project Structure

```
jira_mcp_asses/
├── .env                          # Environment variables (not committed)
├── connection_check.py           # MCP connection test script
├── Level1 Attlasian MCP.ipynb    # Main analysis notebook
├── mcp-env/                      # Python virtual environment
├── package-lock.json             # NPM package lock
└── README.md                     # This file
```

## Security Notes

- **Never commit** the `.env` file to version control
- Keep your API token secure and rotate it periodically
- Use the principle of least privilege for API tokens

## License

[Specify your license here]
