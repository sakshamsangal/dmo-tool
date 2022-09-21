from flask import Flask, render_template, jsonify
from flask_restful import Api
import requests
from werkzeug.exceptions import HTTPException

from config import *
from api.content_type import *

app = Flask(__name__)

api = Api(app)


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code


api.add_resource(ProductList, "/api/content/<content>")
api.add_resource(ContentList, "/api/contents")
api.add_resource(ProductURL, "/api/upload-url", "/api/fetch-urls/<product_name>")


@app.route('/')
def render_home_page():
    return render_template('index.html')


@app.route('/project')
def render_project_page():
    res = requests.get(url=f"http://localhost:{PORT | 5000}/api/contents")
    content_types = res.json()
    return render_template('project.html', content_types=content_types, PORT=PORT)


@app.route('/model')
def render_model_page():
    return render_template('model.html', PORT=PORT)


@app.route('/script')
def render_script_page():
    return render_template('script.html', PORT=PORT)


@app.route('/admin')
def render_admin_page():
    return render_template('admin.html', PORT=PORT)


if __name__ == "__main__":
    app.run(debug=True, port=PORT | 5000)
