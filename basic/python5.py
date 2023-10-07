from User import Buyer, Seller

if __name__ == "__main__":
    buyer = Buyer("김세언", 21, "여성", 10000)
    seller = Seller("김네모", 29, "남성", "네모의 사과농장", 0)

    # 아래의 순서로 코드를 작성하세요
    # 네모가 1개당 1000원짜리 사과를 20개 자신의 상품에 등록합니다

    products = seller.get_products()
    while True:
        seller.add_product('사과', '달달하고 맛있는 사과입니당~', 1000)
        if len(seller.get_products()) == 20:
            break

    # 세언이는 네모의 사과 농장에서 1000원짜리 사과 11개를 사려고 하다가 실패합니다
    # 실패한 경우, 잔액이 xx원 부족합니다 라고 콘솔에 출력해주세요

    i = 0
    while True:
        buyer.add_cart(products[i])
        if i == 8:
            buyer.buy_products()
            break
        i += 1

    # 세언이는 사과 9개를 구매합니다
