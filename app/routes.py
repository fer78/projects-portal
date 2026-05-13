import json
from pathlib import Path
from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def home():
    projects_dir = Path(__file__).parent / "data" / "projects"

    projects = []

    for file in projects_dir.glob("*.json"):
        with open(file, encoding="utf-8") as f:
            projects.append(json.load(f))

    projects.sort(key=lambda p: p["name"])

    return render_template("index.html", projects=projects)