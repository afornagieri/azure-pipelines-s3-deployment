from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import shutil

DIST = Path("dist")
TEMPLATES = Path("templates")

if DIST.exists():
    shutil.rmtree(DIST)
DIST.mkdir()

if TEMPLATES.exists() == False:
    print("Warning: templates folder not found")

env = Environment(
    loader = FileSystemLoader(["src", "templates"])
)

pages = [
    ("index.html", "Home")
]

for page, title in pages:
    index = env.get_template(page)
    html = index.render(
        title = title
    )

    (DIST / page).write_text(
        html,
        encoding="utf-8"
    )

shutil.copytree("static", DIST / "static")