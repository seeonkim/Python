class Product(object):
    def __init__(self, product_row):
        self.__id = product_row[0]
        self.__title = product_row[1]
        self.__price = int(product_row[2])
        self.__content = product_row[3]
        self.__is_selling = bool(product_row[4])
        self.__seller_email = product_row[5]
        self.__buyer_email = product_row[6]

    # 조회
    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_price(self):
        return self.__price

    def get_content(self):
        return self.__content

    def get_is_selling(self):
        return self.__is_selling

    def get_seller_email(self):
        return self.__seller_email

    def get_buyer_email(self):
        return self.__buyer_email

    def convert_dto(self):
        return {
            "id": self.get_id(),
            "title": self.get_title(),
            "content": self.get_content(),
            "price": self.get_price(),
        }

    # 업데이트해야 한다~
    def set_sold_out(self, buyer_email):
        self.__is_selling = False
        self.__buyer_email = buyer_email


if __name__ == "__main__":
    pass
