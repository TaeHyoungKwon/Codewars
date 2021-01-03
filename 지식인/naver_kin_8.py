from random import randint


def get_total_price(menus):
    total = 0
    for menu, price in menus.items():
        total += int(input(f"{menu} 개수 (잔) : ")) * price
    return total


def main(menus):
    while True:
        print("주문할 음료를 말씀하세요.")
        total_price = get_total_price(menus)
        print("총 금액은 :", total_price, "원")

        payment = int(input("지불하실 금액을 입력하세요. >> "))

        if payment >= total_price:
            print("거스름돈은", payment - total_price, "원 입니다.")
            print("주문번호는", randint(1, 100), "번 입니다.")
            break
        else:
            print("금액이 부족합니다.다시 입력하세요.")
            print("\n")


if __name__ == "__main__":
    menus = {"아메리카노": 5000, "카페라떼": 4000, "카라멜마끼아또": 6000, "콜드브루": 5500, "코코아": 3000}
    main(menus)
