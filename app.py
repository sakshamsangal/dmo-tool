from flask import Flask, render_template, request
from flask_restful import Api
import requests

from config import *
from api.content_type import *

app = Flask(__name__)

api = Api(app)

api.add_resource(ProductList, "/api/content/<content>")
api.add_resource(ContentList, "/api/contents")


@app.route('/second', )
def render_second():
    res = requests.get(url=f"http://localhost:{PORT | 5000}/api/contents")
    content_types = res.json()
    return render_template('second.html', content_types=content_types, PORT=PORT)


if __name__ == "__main__":
    app.run(debug=True, port=PORT | 5000)
