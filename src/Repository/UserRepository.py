from src.Domain.User.Buyer import Buyer
from src.Domain.User.Seller import Seller
from src.Domain.User.User import User
from src.Infrastructure.Database import Database


class UserRepository(object):
    def __init__(self):
        self._db = Database()

    def create_user(self, email, password, nickname, money, user_type):
        self._db.write_data_in_csv_file("users.csv", [email, password, nickname, money, user_type])

    def find_user_by_email(self, email):
        users_row = self._db.read_data_in_csv_file("users.csv")
        for user_row in users_row:
            user = User(user_row)
            if user.get_email() == email:
                return user
        return None

    def find_user_by_email_and_password(self, email, password):
        users_row = self._db.read_data_in_csv_file("users.csv")
        for user_row in users_row:
            user = User(user_row)
            if user.get_email() == email and user.get_password() == password:
                if user.get_user_type() == 'seller':
                    return Seller(user_row)
                else:
                    return Buyer(user_row)
        return None


if __name__ == "__main__":
    pass
