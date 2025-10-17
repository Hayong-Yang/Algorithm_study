# 반복되지 않는 문자
# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오. 만약 그런 문자가 없다면 _ 를 반환하시오.

# "abadabac" # 반복되지 않는 문자는 d, c 가 있지만 "첫번째" 문자니까 d를 반환해주면 됩니다!

# 1. for문을 돌면서 알파벳을 하나씩 꺼내온다
# 2. 문자열에서 해당 알파벳이 몇개있는지 count 한다
# 3. if 1보다 크면 continue, 1이면 return하고 끝내기


input = "aabbcddd"

def find_not_repeating_first_character(string):
    not_dup_alphabet = "_"
    for alphabet in string:
        if string.count(alphabet) > 1:
            continue
        else:
            not_dup_alphabet = alphabet
            break
    return not_dup_alphabet

result = find_not_repeating_first_character(input)
print(result)