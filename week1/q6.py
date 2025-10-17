# 소수 나열하기
# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오. 
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.

# 20이 입력된다면, 아래와 같이 반환해야 합니다!
# [2, 3, 5, 7, 11, 13, 17, 19]

# 풀이: 자기 자신과 1로만 나누어 져야함. 
# 1 보다 크고 자기 자신보다 작은 자연수를 하나씩 연산해서 나머지가 0이 끝까지 안나와 -> 소수

# 1. for num in range(2:입력)
# 2. num을 1보다 크고 num보다 작은수로 한번씩 나눈 몫을 구함 // 
# 3. 


input = 20

def find_prime_list_under_number(number):
    prime_num_list =[]
    for num in range(2,number+1):
        for i in range(2,num):
            if num % i == 0: #-> 0이 아니어야 소수
                break
            else:
                prime_num_list.append(num)
    return list(set(prime_num_list))

result = find_prime_list_under_number(input)
print(result)