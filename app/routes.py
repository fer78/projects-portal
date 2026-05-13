import json
from pathlib import Path
from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def home():
    # Ruta al archivo JSON con los proyectos
    data_file = Path(__file__).parent / "data" / "projects.json"

    # Cargar los datos
    with open(data_file, "r", encoding="utf-8") as f:
        projects = json.load(f)

    # Enviar la lista de proyectos a la plantilla
    return render_template("index.html", projects=projects)