class User(object):
    def __init__(self, user_row):
        self._email = user_row[0]
        self._password = user_row[1]
        self._nickname = user_row[2]
        self._money = int(user_row[3])
        self._user_type = user_row[4]

    # 조회
    def get_email(self):
        return self._email

    def get_password(self):
        return self._password

    def get_nickname(self):
        return self._nickname

    def get_money(self):
        return self._money

    def get_user_type(self):
        return self._user_type

    def convert_dto(self):
        return {
            "email": self.get_email(),
            "nickname": self.get_nickname(),
            "money": self.get_money(),
            "user_type": self.get_user_type()
        }

    # 업데이트
    def income(self, money):
        self._money += money

    def withdraw(self, money):
        if self._money < money:
            return False
        else:
            self._money -= money
            return True


if __name__ == "__main__":
    pass
