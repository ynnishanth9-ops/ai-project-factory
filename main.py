import json
from pathlib import Path
from github_client import create_github_repo


OUTPUT_DIR = Path("generated_projects")
IDEAS_FILE = Path("project_ideas.json")


def load_project_ideas():
    """Load AI project ideas from JSON file."""
    if not IDEAS_FILE.exists():
        raise FileNotFoundError("project_ideas.json not found.")

    with open(IDEAS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def generate_readme(project):
    """Generate a professional README.md file for the project."""
    features = "\n".join([f"- {feature}" for feature in project["features"]])
    tech_stack = " · ".join(project["tech_stack"])

    return f"""# {project["title"]}

{project["description"]}

## Features

{features}

## Tech Stack

{tech_stack}

## Project Purpose

This project is part of an AI automation portfolio focused on building practical tools using Python, LangChain, LangGraph, APIs, and workflow automation.

## How It Works

Input data
    ↓
AI processing workflow
    ↓
Generated analysis / response
    ↓
Output report

## Setup

pip install -r requirements.txt
python app.py
"""


def generate_app(project):
    """Generate starter Python app file."""
    title = project["title"]
    description = project["description"]

    return f'''"""
{title}

{description}
"""


def main():
    print("Starting {title}...")
    print("This is a starter AI automation project.")


if __name__ == "__main__":
    main()
'''


def create_project(project):
    """Create project folder and starter files."""
    project_folder = OUTPUT_DIR / project["repo_name"]
    project_folder.mkdir(parents=True, exist_ok=True)

    files = {
        "README.md": generate_readme(project),
        "app.py": generate_app(project),
        "requirements.txt": "python-dotenv\nlangchain\nopenai\n",
        ".env.example": "OPENAI_API_KEY=your_api_key_here\n",
        ".gitignore": ".env\n__pycache__/\n*.pyc\n",
    }

    for file_name, content in files.items():
        file_path = project_folder / file_name
        file_path.write_text(content, encoding="utf-8")

    print(f"Created project: {project_folder}")


def main():
    projects = load_project_ideas()

    for project in projects:
        create_project(project)
        create_github_repo(
            repo_name=project["repo_name"],
            description=project["description"]
        )

    print("All AI projects generated and GitHub repositories created successfully.")


if __name__ == "__main__":
    main()
