from flask import render_template
from app.main import bp

@bp.route('/')
def index():
    title = "Welcome to Your Flask App"
    description = "This is a sample Flask application using Jinja2 templates."
    return render_template('main/index.html', title=title, description=description)
