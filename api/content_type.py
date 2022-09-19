from flask_restful import Resource
from flask import request
from db import query, update


class ContentList(Resource):
    def get(self):
        return query.get_content_names()


class ProductList(Resource):
    def get(self, content):
        return query.get_product_names(content)


class ProductURL(Resource):
    def get(self, product_name):
        return query.get_urls(product_name)

    def post(self):
        product_name = request.json.get('product_name')
        links = request.json
        del links['product_name']
        return update.set_links(product_name, links)