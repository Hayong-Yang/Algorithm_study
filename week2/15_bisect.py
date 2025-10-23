# 이진탐색 모듈 bisect 연습해보기 -> 시간복잡도 O(LogN)

import bisect

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두", "치킨"]

def is_available_to_order(menus, orders):
    sotred_menus = sorted(menus)

    for food in orders:
        idx = bisect.bisect_left(sotred_menus, food)
        if idx >= len(sotred_menus) or sotred_menus[idx] != food:
            print(f"{food} 불가능!")
            return False
        print(f"{food} 가능!")
    return True

result = is_available_to_order(shop_menus, shop_orders)
print(result)