input = [4, 6, 2, 9, 1] # length = 5, i=0,1,2 
# 16294
# 12694
# 12496

def selection_sort(array):
    length = len(array)

    for i in range(length-1):
        min_num = array[i]
        min_num_idx = i
        for j in range(i+1, length):
            if array[j] < min_num:
                min_num = array[j]
                min_num_idx = j
        array[i], array[min_num_idx] = array[min_num_idx], array[i]
    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))