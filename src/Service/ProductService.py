from src.Repository.repository import Repository


class ProductService(object):
    def __init__(self):
        self.repository = Repository()

    def get_all_selling_products(self, email):
        user = self.repository.User.find_user_by_email(email)
        if user is None:
            print("잘못된 접근입니다")
            return None

        result = []
        products = self.repository.Product.find_selling_products()
        for product in products:
            result.append(product.convert_dto())

        return result

    def get_my_selling_products(self, email):
        user = self.repository.User.find_user_by_email(email)
        if user is None:
            print("잘못된 접근입니다")
            return None

        result = []
        products = self.repository.Product.find_seller_products_by_email(email)
        for product in products:
            result.append(product.convert_dto())

        return result

    def add_selling_product(self, title, price, content, seller_email):
        self.repository.Product.create_product(title, price, content, seller_email)

    def buy_product(self, email, product_id):
        buyer = self.repository.User.find_user_by_email(email)
        if buyer is None:
            print("잘못된 접근입니다!")
            return None

        product = self.repository.Product.find_product_by_id(product_id)
        if product is None:
            print("상품이 없습니다")
            return None
        if product.get_is_selling() == "N":
            print("판매중인 상태가 아닙니다")
            return None
        if buyer.get_money() < product.get_price():
            print("잔액이 없습니다")
            return None

        seller = self.repository.User.find_user_by_email(product.get_seller_email())
        if seller is None:
            print("잘못된 접근입니다")
            return None

        result = buyer.withdraw(product.get_price())
        if not result:
            print("잔액이 부족합니다")
        seller.income(product.get_price())
        product.set_sold_out(buyer.get_email())

        self.repository.User.save(seller)
        self.repository.User.save(buyer)
        self.repository.Product.save(product)


        #현재 각 리파지토리에 save 함수가 없기 때문에 그것을 만들어야 하고..
        #user 도메인과 product 도메인 안에 있는 함수 (withdraw 랑 setsoldout은 리파지토리의 save 함수를 이용할것이다.)
        #돈 인출 및 품절 상태표시, buyer email 표시 모두 열 하나를 추가하는 작업이 아니라 열 내의 정보를 변경하는 작업
        #품절 상태 표시할때.. csv파일의 문자열 정보를 연산할때 사용하려면, bool 처리를 해야 한당.

        #즉 db의 update 함수를 이용하는 것이기 때문
        #db의 update 함수는 곧 base repository가 사용한다
        #이 base repository는 product service를 사용한다

        return product
