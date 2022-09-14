from flask_restful import Resource
from db import query


class ContentList(Resource):
    def get(self):
        return query.get_content_names()


class ProductList(Resource):
    def get(self, content):
        return query.get_product_names(content)