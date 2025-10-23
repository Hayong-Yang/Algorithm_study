# [코드스니펫] 버블 정렬
input = [4, 6, 2, 9, 1]

def bubble_sort(array):
    first_idx = 0
    second_idx = 1
    is_sorted = False
    arr_length = len(array)

    def recursive_sorted_check(array, length):
        if length <= 1:
            return True
        if array[length-2] > array[length-1]:
            return False
        return recursive_sorted_check(array, length-1)

    while is_sorted is not True:
        if second_idx == arr_length:
            # 끝까지 한번 수행하면 체크!
            result = recursive_sorted_check(array, arr_length)
            if result == True:
                is_sorted = True
                break
            else:
                first_idx = 0
                second_idx = 1
                print(array)
                continue
        if array[first_idx] > array[second_idx]:
            array[first_idx], array[second_idx] = array[second_idx], array[first_idx]
        first_idx += 1
        second_idx += 1
        
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

# print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
# print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
# print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))