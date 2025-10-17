# 문자열 뒤집기\
# Q. 0과 1로만 이루어진 문자열이 주어졌을 때, 이 문자열에 있는 모든 숫자를 전부 같게 만들려고 한다. 할 수 있는 행동은 문자열에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.

"""
예를 들어 S=0001100 일 때,

전체를 뒤집으면 1110011이 된다.
4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 2번 만에 모두 같은 숫자로 만들 수 있다.
하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.

주어진 문자열을 모두 0 혹은 모두 1로 같게 만드는 최소 횟수를 반환하시오.
"""

input = "0111101101010100"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    to_zero_count = 0
    to_one_count = 0
    
    if string[0] == "0":
        to_one_count += 1
    elif string[0] =="1":
        to_zero_count += 1
    
    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            if string[i+1] =="0":
                to_one_count += 1
            if string[i+1] == "1":
                to_zero_count += 1
    return min(to_zero_count, to_one_count)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)