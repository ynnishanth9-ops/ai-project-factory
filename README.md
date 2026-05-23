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