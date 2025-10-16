# 최빈값 찾기
# Q.  다음과 같은 문자열을 입력받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오. (단 최빈값을 가진 알파벳이 여러개일 경우 알파벳 순서가 가장 앞에 위치한 알파벳을 출력하시오)

# "hello my name is dingcodingco"

# 하용 방법
# 1. 문자열에 사용된 알파벳 리스트를 구한다
# 2. 알파벳 리스트를 for문 돌면서 문자열에서 해당 알파벳이 몇개 있나 count 한다. -> dict 형태로 반환 {알파벳 : count}
# 3. 알파벳으로 오름차순 정렬
# 4. 알파벳 첫번째 값을 max_count로 두고 하나씩 비교 클때만 maxcount. 같거나 작을때는 넘어가기

# # 1.
# phrase = "hello my name is dingcodingco"
# alphabet_list = list(set(phrase))
# print(alphabet_list)

# # 2.
# count_dict = {}
# for alphabet in alphabet_list:

#     if alphabet == " ":
#         continue

#     count = phrase.count(alphabet)
#     count_dict[alphabet] = count
# print(count_dict)  

# # 3.  
# sorted_dict = sorted(count_dict.keys())
# print(sorted_dict)

# # 4.
# max_count = count_dict[sorted_dict[0]]
# max_count_alphabet ={sorted_dict[0]:count_dict[sorted_dict[0]]}
# for alphabet in sorted_dict:
#     if count_dict[alphabet] > max_count:
#         max_count = count_dict[alphabet]
#         max_count_alphabet = {alphabet:max_count}
# print(max_count_alphabet)

# 함수화

def find_max_occurred_alphabet(string):
    # 1.
    alphabet_list = list(set(string))
    # print(alphabet_list)

    # 2. 
    count_dict = {}
    for alphabet in alphabet_list:

        if alphabet == " ":
            continue

        count = string.count(alphabet)
        count_dict[alphabet] = count
    # print(count_dict)  

    # 3. 
    sorted_dict = sorted(count_dict.keys())
    # print(sorted_dict)

    # 4.
    max_count = count_dict[sorted_dict[0]]
    max_count_alphabet ={sorted_dict[0]:count_dict[sorted_dict[0]]}
    for alphabet in sorted_dict:
        if count_dict[alphabet] > max_count:
            max_count = count_dict[alphabet]
            max_count_alphabet = {alphabet:max_count}
    # print(max_count_alphabet)

    return max_count_alphabet


string1="hello my name is dingcodingco"
string2="we love algorithm"
string3="best of best youtube"
max_count_alphabet = find_max_occurred_alphabet(string3)
print(max_count_alphabet)