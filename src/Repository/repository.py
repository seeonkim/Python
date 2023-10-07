from src.Repository.ProductRepository import ProductRepository
from src.Repository.UserRepository import UserRepository


class Repository(object):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.User = UserRepository()
        self.Product = ProductRepository()

    def save(self, domain_direct):
        dict = domain_direct._dict_
        return dict

if __name__ == "__main__":
    pass
