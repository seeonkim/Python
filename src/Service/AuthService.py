from src.Repository.repository import Repository


class AuthService(object):
    def __init__(self):
        self.repository = Repository()

    def sign_up(self, email, password, nickname, money, user_type):
        is_user_already_exist = self.repository.User.find_user_by_email(email)
        if is_user_already_exist:
            print("중복된 이메일입니다. 다시 입력해 주세요.")
            return False
        self.repository.User.create_user(email, password, nickname, money, user_type)
        print("회원가입이 성공적으로 완료되었습니다!")
        return True

    def login(self, email, password):
        user = self.repository.User.find_user_by_email_and_password(email, password)
        if user is None:
            return None
        else:
            return user.convert_dto()


if __name__ == "__main__":
    pass
