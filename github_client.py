import os
import requests
from dotenv import load_dotenv


load_dotenv()


GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def create_github_repo(repo_name, description):
    """Create a new public GitHub repository."""
    if not GITHUB_USERNAME or not GITHUB_TOKEN:
        raise ValueError("GITHUB_USERNAME and GITHUB_TOKEN must be set in .env")

    url = "https://api.github.com/user/repos"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    payload = {
        "name": repo_name,
        "description": description,
        "private": False,
        "auto_init": False
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        repo_url = response.json()["html_url"]
        print(f"Created GitHub repo: {repo_url}")
        return repo_url

    if response.status_code == 422:
        print(f"Repository already exists: {repo_name}")
        return f"https://github.com/{GITHUB_USERNAME}/{repo_name}"

    print("Failed to create repository")
    print("Status code:", response.status_code)
    print("Response:", response.text)
    return None
