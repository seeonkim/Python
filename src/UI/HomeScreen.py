from src.Service.Service import Service


class HomeScreen(object):
    def __init__(self):
        self.service = Service()
        self.user = None

    def main(self, user):
        self.user = user
        if self.user['user_type'] == 'buyer':
            print("구매자 메인 화면입니다")
            self.buyer_main_screen()
        if self.user['user_type'] == 'seller':
            print("판매자 메인 화면입니다")
            self.seller_main_screen()

    def seller_main_screen(self):
        print("=====이메일 정보입니다=====")
        print(self.user['email'])

        print("=====보유중인 상품 목록입니다=====")
        products = self.service.product().get_my_selling_products(self.user['email'])
        for product in products:
            print(f"{product['id']}, {product['title']}, {product['price']}")

        print("=====계좌 잔액입니다=====")
        print(self.user['money'])

        print("=====상품 추가 페이지 입니다=====")
        email = self.user['email']
        title = input("추가하고 싶은 상품의 이름을 입력하세요: ")
        price = input("추가하고 싶은 상품의 가격을 입력하세요: ")
        content = input("추가하고 싶은 상품의 콘텐츠를 입력하세요: ")

        self.service.product().add_selling_product(title, price, content, email)
        print("상품이 추가되었습니다.")

        self.seller_main_screen()

    def buyer_main_screen(self):
        print("=====이메일 정보입니다=====")
        print(self.user['email'])

        print("=====판매중인 상품 목록입니다=====")
        products = self.service.product().get_all_selling_products(self.user['email'])
        for product in products:
            print(f"{product['id']}, {product['title']}, {product['content']}, {product['price']}")

        print("=====계좌 잔액입니다=====")
        print(self.user['money'])

        print("=====상품 구매 페이지 입니다=====")
        product_id = input("구매하고 싶은 상품 아이디를 입력하세요: ")
        bought_product = self.service.product().buy_product(self.user['email'], product_id)
        if bought_product:
            print("구매가 완료되었습니다.")

        self.buyer_main_screen()
