"""
- Q1. ✍️ 쓱 최대로 할인 적용하기
    ❓ Q. 
    다음과 같이 숫자로 이루어진 배열이 두 개가 있다. 
    하나는 상품의 가격을 담은 배열이고, 하나는 쿠폰을 담은 배열이다. 
    쿠폰의 할인율에 따라 상품의 가격을 할인 받을 수 있다. 
    이 때, 최대한 할인을 많이 받는다면 얼마를 내야 하는가?
    단, 할인쿠폰은 한 제품에 한 번씩만 적용 가능하다
"""
# 가장 가격이 큰 상품에 할인율 가장 큰 쿠폰을 적용
# -> 가격순, 쿠폰할인율 순으로 내림차순 정렬
# -> zip 함수 사용해서 순차적으로 적용. 
# -> 상품이 쿠폰보다 많은경우, 나머지 상품은 그냥 계산

shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

def get_max_discounted_price(prices, coupons):
    total_price = 0
    #1. 내림차순 정렬
    sorted_prices = sorted(prices, reverse=True)
    sorted_coupons = sorted(coupons, reverse=True)
    print(sorted_prices)
    print(sorted_coupons)

    prices_length = len(sorted_prices)
    coupons_length = len(sorted_coupons)
    #2. zip 돌면서 짧은 배열기준으로 반복
    for price, coupon in zip(sorted_prices,sorted_coupons):
        total_price += price * ((100-coupon)/100)
        print(total_price)
    #3. 상품이 쿠폰보다 많은경우, 나머지 상품은 그냥 계산
    if prices_length > coupons_length:
        for price in sorted_prices[coupons_length:prices_length]:
            total_price += price
        return total_price
    return total_price
    
print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
# print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
# print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
# print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))