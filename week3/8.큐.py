"""
<aside>
❓ Q.

초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 함수를 완성하세요.

prices = [1, 2, 3, 2, 3]
answer = [4, 3, 1, 1, 0]

</aside>
"""

from collections import deque

prices = [1, 2, 3, 2, 3]
# 하나씩 popleft해서 cur에 담고
# cur과 나머지 큐를 비교.
# 비교할게 있다면 1 없다면 0
# cur보다 작으면 끝 -> count 반환해서 리스트에 담음
# cur 보다 크거나 같으면 반복하며 count 증가
def get_price_not_fall_periods(prices):
    answer =[]
    prices_que = deque(prices)
    cur = prices_que.popleft() 
    
    while len(prices_que) > 0:
        count = 0
        for i in range(len(prices_que)): 
            count += 1
            if prices_que[i] < cur:
                break
        answer.append(count) 
        cur = prices_que.popleft()  
    
    answer.append(0) 
    return answer

print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))