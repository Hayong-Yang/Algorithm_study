'''
회문은 똑바로 읽으나 거꾸로 읽으나 똑같은 단어나 문장을 의미합니다.

우영우
역삼역
기러기
토마토
오디오
아시아
일요일
소주만병만주소
가련하시다 사장 집 아들 딸들아 집 장사 다시 하련가

같은 단어를 회문 이라고 합니다!

컴퓨터는 문자열을 보고 아래처럼 어떻게 회문인지 확인할 수 있을까요?
'''

# Q. 다음과 같이 문자열이 입력되었을 때, 회문이라면 True 아니라면 False 를 반환하시오.

input = "abcba"

def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    return False


print(is_palindrome(input))