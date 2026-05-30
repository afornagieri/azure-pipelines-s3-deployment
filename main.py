from flask import Flask, render_template_string

from static.index_html import index_page

app = Flask(__name__)

@app.route("/")
def index():
    page = index_page()
    return render_template_string(page)