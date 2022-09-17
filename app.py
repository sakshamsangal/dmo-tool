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
api.add_resource(ProductURL, "/api/upload-url", "/api/fetch-url/<product_name>")


@app.route('/')
def render_home():
    return render_template('index.html')


@app.route('/second')
def render_second():
    res = requests.get(url=f"http://localhost:{PORT | 5000}/api/contents")
    content_types = res.json()
    return render_template('second.html', content_types=content_types, PORT=PORT)


if __name__ == "__main__":
    app.run(debug=True, port=PORT | 5000)
