from src.Service.Service import Service


class AuthScreen(object):
    def __init__(self):
        self.service = Service()

    def auth(self):
        auth_choice = int(input("회원 가입(0) | 로그인(1): "))
        if auth_choice == 0:
            is_signed_up = self.sign_up()
            if is_signed_up is False:
                print("회원 가입에 실패했어요")
            else:
                print("회원 가입에 성공했어요")
            self.auth()
        else:
            user = self.login()
            if user is None:
                print("이메일 또는 비밀번호 오류입니다")
                self.auth()
            else:
                print("로그인에 성공했어요")
                return user

    def sign_up(self):
        email = input("이메일을 입력하세요: ")
        password = input("비밀번호를 입력하세요: ")
        nickname = input("유저의 이름을 입력하세요: ")
        money = input("자산을 입력하세요: ")
        user_type = input("유저의 타입(buyer/seller)을 입력하세요: ")

        is_signed_up = self.service.auth().sign_up(email, password, nickname, money, user_type)

        return is_signed_up

    def login(self):
        email = input("이메일을 입력하세요: ")
        password = input("비밀번호를 입력하세요: ")
        user = self.service.auth().login(email, password)

        return user
