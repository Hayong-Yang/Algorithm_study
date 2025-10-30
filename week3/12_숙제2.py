"""
Q. 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻이다. 예를 들어

()() 또는 (())() 는 올바르다.
)()( 또는 (()( 는 올바르지 않다.

이 때, '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 True 를 반환하고 아니라면 False 를 반환하시오.
"""

# 문자열을 하나씩 빼면서 (가 몇개 나오는지 개수세기
# -> ( 가 연달아 나오는 개수만큼 )가 연달아 나와야 함
# -> 만약 개수가 다르다면 바로 return False

# -> deque 를 사용해서 큐의 맨앞부터 popleft() 추출
# -> ( 빼오면 is_closed= False, count +=1
# -> 그리고 False 이고 ) 빼오면, 그 count가 같아질때 까지는 (가 나오면 안됨. -> 바로 종료 False
# -> is_closed = True일때 ) 빼오면 바로 종료
# -> 만약 count가 같아지면 is_closed =True 만들고 모든 카운트 초기화  
# 끝까지 가서 is_closed 가 True 이면 true 반환

from collections import deque

def is_correct_parenthesis(string):
    string_que = deque(string)
    start_count = 0
    end_count = 0
    is_closed = True
    cur_pop = ""
    while len(string_que) > 0:
        pop_str = string_que.popleft()
        # 모두 닫히면 초기화
        if start_count == end_count:
            is_closed = True
            start_count= 0
            end_count = 0
        # 처음 ) 나오면 False 반환 후 종료
        if is_closed == True and pop_str == ")":
            return False
        # 처음 ( 나오면 열고 counting 시작
        if is_closed == True and pop_str == "(":
            start_count =0
            is_closed = False
            start_count += 1
            cur_pop = pop_str
            continue
        # 열린 후 ( 나오면 조건체크: 닫히지 않았는데 ) 나오기 시작하면 닫힐때 까지 ) 만 나와야 함. 그렇지 않다면 False 후 종료
        if is_closed == False and pop_str == "(":
            if cur_pop == ")":
                return False
            start_count += 1
            cur_pop = pop_str
            continue
        if is_closed == False and pop_str == ")":
            end_count += 1
            cur_pop = pop_str
            if start_count == end_count:
                is_closed = True
            continue
    return is_closed


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))