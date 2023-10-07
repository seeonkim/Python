from src.Service.AuthService import AuthService
from src.Service.ProductService import ProductService


class Service:
    def __init__(self):
        self.__auth = AuthService()
        self.__product = ProductService()

    def auth(self):
        return self.__auth

    def product(self):
        return self.__product
