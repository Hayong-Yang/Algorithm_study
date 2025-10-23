"""
Q. 배달의 민족 서버 개발자로 입사했다.
상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때, 유저가 ["오뎅", "콜라", "만두"] 를 주문했다.

그렇다면, 현재 주문 가능한 상태인지 여부를 반환하시오.
"""
# -> 순차탐색이 더 효율적이네.
# 그런데 in 연산자로 순차탐색할때 list 보다 set으로 변환하고 작업하는 것이 효율적이다.

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

# # 순차탐색
# def is_available_to_order(menus, orders):
#     for food in orders:
#         if food not in menus:
#             return False
#     return True

# result = is_available_to_order(shop_menus, shop_orders)
# print(result)

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


# 이진탐색 -> 정렬이 필수!!
def is_available_to_order(menus, orders):
    # 정렬
    sorted_menus = sorted(menus)
    sorted_orders = sorted(orders)

    # 이진탐색
    is_found = None
    for food_idx, food in enumerate(sorted_orders):
        min_idx = 0
        max_idx = len(sorted_menus)
        guess_idx = (min_idx + max_idx) // 2

        while min_idx <= max_idx:
            if sorted_menus[guess_idx] == food:
                is_found = True
                return is_found
            # 가나다 와 같은 한글도 크기비교가 가능하다! -> 유니코드 값으로 계산됨
            elif sorted_menus[guess_idx] < food:
                min_idx = guess_idx + 1
            elif sorted_menus[guess_idx] > food:
                max_idx = guess_idx - 1
            guess_idx = (min_idx + max_idx) // 2
        is_found = False
        return is_found

    if is_found == False:
        return False
    return True

result = is_available_to_order(shop_menus, shop_orders)
print(result)