from db.connect import init


def fetch_data():
    query_str = '''
    SELECT * FROM products
    '''

    db, cursor = init()

    rows = list(cursor.execute(query_str))
    db.close()

    products = map(lambda product:
                   {
                       'content_type': product[0].strip().upper(),
                       'product_name': product[1].strip().upper(),
                       'product_group': product[2].strip().upper()
                   }, rows)
    return list(products)


def get_product_names(content_type):
    products = fetch_data()
    product_names = []
    for product in products:
        if content_type.strip().upper() == product['content_type']:
            product_names.append(product['product_name'])
    return product_names


def get_content_names():
    products = fetch_data()
    content_names = set()
    for product in products:
        content_names.add(product['content_type'])
    return list(content_names)
