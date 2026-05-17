from pathlib import Path
import json
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, field_validator

from main import run_factory


app = FastAPI(title="AI Project Factory API")


class ProjectIdea(BaseModel):
    repo_name: str
    title: str
    description: str
    tech_stack: Union[list[str], str]
    features: Union[list[str], str]

    @field_validator("tech_stack", "features")
    @classmethod
    def convert_string_to_list(cls, value):
        if isinstance(value, str):
            return [item.strip() for item in value.split(",") if item.strip()]
        return value


@app.get("/")
def home():
    return {
        "message": "AI Project Factory API is running"
    }


@app.post("/generate")
def generate_project(project: ProjectIdea):
    input_file = Path("input_project.json")

    project_data = project.model_dump()

    input_file.write_text(
        json.dumps(project_data, indent=2),
        encoding="utf-8"
    )

    run_factory(input_file)

    return {
        "status": "success",
        "repo_name": project.repo_name,
        "github_url": f"https://github.com/ynnishanth9-ops/{project.repo_name}"
    }