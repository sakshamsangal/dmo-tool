from db.connect import init


def set_links(product_name, links):
    db, cursor = init()
    for key, value in links.items():
        update_query = f"UPDATE products SET {key} = ? WHERE upper(product_name) = ?"
        cursor.execute(update_query, (value, product_name))
    db.commit()
    db.close()
    return 'success'

