input = 50

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}

def fibo_dynamic_programming(n, fibo_memo):
    if fibo_memo.get(n):
        return fibo_memo.get(n)
    result = fibo_dynamic_programming(n-1, fibo_memo) + fibo_dynamic_programming(n-2, fibo_memo)
    fibo_memo[n] = result
    return result

print(fibo_dynamic_programming(input, memo))

# 바텀업(반복문 순차)과 탑다운(재귀 + 메모이제이션)
"""
언제 무엇을 사용하는것이 좋은가?

바텀업은 아래서 부터 순차적으로 계산해서 목적에 도달하는 방법.
따라서 순차적으로 값을 구할 수 있는 문제에서는 더 빠름.
심지어 규모가 큰 입력값에서 강점이 있음.
단, 그래프/트리 구조에서 순서가 없는 경우 사용불가능

탑다운은 필요한 계산만 찾으면서 메모이제이션 참조하며 목적에 도달하는 방법.
순차적일 필요가 없기때문에 순서가 없는 문제에서 강점.
단 규모가 큰 입력값에서 함수호출 제한 및 recursion error 발생 가능.

"""