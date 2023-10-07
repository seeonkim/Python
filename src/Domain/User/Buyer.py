from src.Domain.User.User import User


class Buyer(User):
    def __init__(self, user_row):
        super().__init__(user_row)


if __name__ == "__main__":
    pass
