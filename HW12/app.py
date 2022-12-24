from flask import Flask, request, render_template, send_from_directory

from loader.loader import loader_bp
from main.main import main_bp

# from functions import ...

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main_bp)
app.register_blueprint(loader_bp)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
