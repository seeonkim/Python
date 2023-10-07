import random
from src.Domain.product import Product
from src.Infrastructure.Database import Database


class ProductRepository(object):
    def __init__(self):
        self._db = Database()

    def create_product_id(self):
        product_id = random.randrange(0, 9999)
        product = self.find_product_by_id(product_id)
        if product:
            self.create_product_id()
        return product_id

    def create_product(self, title, price, content, seller_email):
        product_id = self.create_product_id()
        is_selling = True
        buyer_email = None
        self._db.write_data_in_csv_file("products.csv",
                                        [product_id, title, price, content, is_selling, seller_email, buyer_email])

    def find_product_by_id(self, product_id):
        products_row = self._db.read_data_in_csv_file("products.csv")
        for product_row in products_row:
            product = Product(product_row)
            if product.get_id() == product_id:
                return Product(product_row)
        return None

    def find_seller_products_by_email(self, email):
        products = []
        product_rows = self._db.read_data_in_csv_file("products.csv")
        for product_row in product_rows:
            product = Product(product_row)
            if product.get_seller_email() == email:
                products.append(product)
        return products

    def find_selling_products(self):
        products = []
        product_rows = self._db.read_data_in_csv_file("products.csv")
        for product_row in product_rows:
            product = Product(product_row)
            if product.get_is_selling():
                products.append(product)
        return products


if __name__ == "__main__":
    pass
