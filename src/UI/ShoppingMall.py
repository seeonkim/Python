from src.UI.AuthScreen import AuthScreen
from src.UI.HomeScreen import HomeScreen


class ShoppingMall(object):
    def __init__(self):
        self.auth_screen = AuthScreen()
        self.home_screen = HomeScreen()

    def init(self):
        user = self.auth_screen.auth()
        self.home_screen.main(user)


if __name__ == "__main__":
    pass
