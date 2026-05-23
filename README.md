# AI Project Factory

AI Project Factory is an end-to-end AI automation engine that converts rough project ideas into structured GitHub repositories.

The system uses n8n, OpenAI, FastAPI, Python, and the GitHub API to generate project files, create repositories, and push generated code automatically.

## Project Overview

This project was built as part of my learning journey in LangChain, AI automation, and workflow engineering.

Instead of manually creating project repositories, this automation takes a rough idea, converts it into structured project metadata, generates a project folder, creates a GitHub repository, and pushes the generated files automatically.

## Automation Architecture

```text
Rough Project Idea
        ↓
n8n Workflow
        ↓
OpenAI Structured JSON Generation
        ↓
FastAPI Controller
        ↓
Python Project Factory Engine
        ↓
GitHub API
        ↓
Generated GitHub Repository
```

## How It Works

1. A rough project idea is entered in n8n.
2. OpenAI converts the idea into structured project data.
3. n8n sends the structured JSON to the FastAPI endpoint.
4. FastAPI triggers the Python project generation engine.
5. AI Project Factory creates:
   - README.md
   - app.py
   - requirements.txt
   - .env.example
   - .gitignore
6. The GitHub repository is created automatically.
7. Generated files are pushed to the new GitHub repository.

## Features

- Generate AI project repositories from structured JSON input
- Convert rough ideas into project metadata using OpenAI
- Control the workflow using n8n
- Trigger the Python engine through FastAPI
- Create professional README files automatically
- Generate starter Python application files
- Generate requirements.txt and .env.example files
- Create GitHub repositories automatically
- Push generated files to GitHub
- Support dynamic input from external workflow tools

## Tech Stack

- Python
- FastAPI
- n8n
- OpenAI API
- GitHub API
- Git
- JSON
- Automation workflows

## Project Structure

```text
ai-project-factory/
├── main.py
├── api_server.py
├── github_client.py
├── project_ideas.json
├── input_project.json
├── requirements.txt
├── .env.example
├── README.md
└── generated_projects/
```

## Local Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GITHUB_USERNAME=your_github_username
GITHUB_TOKEN=your_github_token_here
```

Do not commit the real `.env` file to GitHub.

## Run Manually

Generate projects from the default project list:

```bash
python3 main.py
```

Generate a project from a custom input file:

```bash
python3 main.py --input input_project.json
```

## Run the FastAPI Controller

Start the local API server:

```bash
python3 -m uvicorn api_server:app --reload
```

The API runs at:

```text
http://127.0.0.1:8000
```

Main endpoint:

```text
POST /generate
```

## Example API Input

```json
{
  "repo_name": "ai-student-study-planner",
  "title": "AI Student Study Planner",
  "description": "An AI automation tool that creates personalized study plans based on subjects, deadlines, and available time.",
  "tech_stack": "Python, LangChain, OpenAI API",
  "features": "Subject tracking, Deadline analysis, Study plan generation, Markdown report output"
}
```

## n8n Workflow

The n8n workflow acts as the controller for the automation.

Workflow structure:

```text
Manual Trigger
        ↓
Set Rough Project Idea
        ↓
OpenAI
        ↓
Code Node
        ↓
HTTP Request
        ↓
AI Project Factory API
```

The HTTP Request node sends the generated project JSON to:

```text
http://127.0.0.1:8000/generate
```

## Sample Output

The automation successfully generated and published multiple AI project repositories to GitHub.

Example generated repositories:

- AI Personal Finance Agent
- AI Student Study Planner
- AI Meeting Notes Agent
- Automated Chatbot System
- Natural Language Processing Application

Each generated repository includes:

```text
project-name/
├── README.md
├── app.py
├── requirements.txt
├── .env.example
└── .gitignore
```

Example successful automation response:

```text
status: success
repo_name: ai-personal-finance-agent
github_url: https://github.com/ynnishanth9-ops/ai-personal-finance-agent
```

## Example Generated Projects

This engine has generated AI project repositories such as:

- AI Resume Optimizer Agent
- AI Research Assistant RAG
- AI Email Task Agent
- AI Meeting Notes Agent
- AI Personal Finance Agent
- AI Student Study Planner
- Automated Chatbot System
- Natural Language Processing Application

## What I Learned

Through this project, I practiced:

- Building AI automation workflows
- Connecting n8n with a Python backend
- Using OpenAI output as structured JSON
- Creating FastAPI endpoints
- Automating GitHub repository creation
- Generating project files programmatically
- Designing an end-to-end AI engineering workflow

## Current Status

The project currently supports:

- Manual JSON input
- Dynamic input file support
- FastAPI API control
- n8n workflow control
- OpenAI-generated project metadata
- GitHub repository creation
- Automated file push to GitHub

## Future Improvements

- Add project quality scoring
- Add duplicate repository detection
- Add automatic GitHub topic tagging
- Add generated screenshots or sample output files
- Add approval step before publishing
- Add Google Sheets or Notion logging
- Add website/RSS project idea collection
- Add licence and attribution checks

## Repository

GitHub: https://github.com/ynnishanth9-ops/ai-project-factory
