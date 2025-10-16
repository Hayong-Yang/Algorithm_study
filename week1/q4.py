#  곱하기 or 더하기

# Q. 다음과 같이 0 혹은 양의 정수로만 이루어진 배열이 있을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 '✕' 혹은 '+' 연산자를 넣어 결과적으로 가장 큰 수를 구하는 프로그램을 작성하시오. 
# 단, '+' 보다 '✕' 를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서 순서대로 이루어진다.

# [0, 3, 5, 6, 1, 2, 4]

# 방법: 
# 1. 변수 초기화
# 2. for문으로 하나씩 꺼내온다
# 3. 변수에 꺼내온 값을 연산한다.
# 4. 연산 시 0 또는 1이 있다면 덧셈을 해야함

def find_max_plus_or_multiply(array):
    final_num = 0
    # 연산
    for num in array:
        if num == 0 or num == 1:
            final_num += num
        else:
            if final_num == 0:
                final_num += num
            else:
                final_num *= num
        # print(final_num)
    return final_num

result = find_max_plus_or_multiply([1,1,1,3,3,2,5])
print(result)