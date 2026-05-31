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
    loader = FileSystemLoader("templates")
)

pages = [
    ("base.html", "Home")
]

for page, title in pages:
    template = env.get_template(page)
    html = template.render(
        title = title
    )

    (DIST / page).write_text(
        html,
        encoding="utf-8"
    )

shutil.copytree("static", DIST / "static")