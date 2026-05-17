import argparse
import json
from pathlib import Path

from github_client import create_github_repo, push_project_to_github


OUTPUT_DIR = Path("generated_projects")
DEFAULT_IDEAS_FILE = Path("project_ideas.json")


def load_project_ideas(file_path):
    """Load project ideas from a JSON file."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Project ideas file not found: {file_path}")

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if isinstance(data, dict):
        return [data]

    if isinstance(data, list):
        return data

    raise ValueError("Input JSON must be either a project object or a list of projects.")


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


def process_input(user_input):
    """Process sample input for this AI automation project."""
    result = {{
        "input": user_input,
        "summary": "This is a generated starter workflow.",
        "next_step": "Replace this logic with LangChain, LangGraph, or API-based automation."
    }}

    return result


def main():
    sample_input = "Sample input for {title}"

    result = process_input(sample_input)

    print("{title}")
    print("-" * len("{title}"))
    print("Input:", result["input"])
    print("Summary:", result["summary"])
    print("Next Step:", result["next_step"])


if __name__ == "__main__":
    main()
'''


def generate_requirements(project):
    """Generate requirements.txt based on project tech stack."""
    tech_stack = [tech.lower() for tech in project["tech_stack"]]

    requirements = ["python-dotenv"]

    if "langchain" in tech_stack:
        requirements.append("langchain")

    if "langgraph" in tech_stack:
        requirements.append("langgraph")

    if "openai api" in tech_stack:
        requirements.append("openai")

    if "faiss" in tech_stack:
        requirements.append("faiss-cpu")

    return "\n".join(requirements) + "\n"


def create_project(project):
    """Create project folder and starter files."""
    project_folder = OUTPUT_DIR / project["repo_name"]
    project_folder.mkdir(parents=True, exist_ok=True)

    files = {
        "README.md": generate_readme(project),
        "app.py": generate_app(project),
        "requirements.txt": generate_requirements(project),
        ".env.example": "OPENAI_API_KEY=your_api_key_here\n",
        ".gitignore": ".env\n__pycache__/\n*.pyc\n",
    }

    for file_name, content in files.items():
        file_path = project_folder / file_name
        file_path.write_text(content, encoding="utf-8")

    print(f"Created project: {project_folder}")
    return project_folder


def run_factory(input_file):
    """Generate projects, create GitHub repos, and push files."""
    projects = load_project_ideas(input_file)

    for project in projects:
        project_folder = create_project(project)

        create_github_repo(
            repo_name=project["repo_name"],
            description=project["description"]
        )

        push_project_to_github(
            project_folder=project_folder,
            repo_name=project["repo_name"]
        )

    print("All projects generated, repositories created, and files pushed successfully.")


def main():
    parser = argparse.ArgumentParser(description="AI Project Factory")
    parser.add_argument(
        "--input",
        default=str(DEFAULT_IDEAS_FILE),
        help="Path to project idea JSON file"
    )

    args = parser.parse_args()
    run_factory(args.input)


if __name__ == "__main__":
    main()