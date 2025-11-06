input = 20

# 길이 20, 인덱스 19

def fibo_recursion(n):
    fibo_list = [1,1]
    for i in range(2,n):
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
    return fibo_list[n-1]

print(fibo_recursion(input))  # 6765