array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]
4
1

def merge(array1, array2):
    result_array = []
    array1_idx = 0
    array2_idx = 0

    array1_length = len(array1)
    array2_length = len(array2)

    total_length = array1_length + array2_length
    while len(result_array) < total_length:
        if array1_idx >= array1_length:
            result_array.append(array2[array2_idx])
            array2_idx +=1
            continue
        if array2_idx >= array2_length:
            result_array.append(array1[array1_idx])
            array1_idx +=1
            continue
        if array1[array1_idx] <= array2[array2_idx]:
            result_array.append(array1[array1_idx])
            array1_idx += 1
        elif array1[array1_idx] > array2[array2_idx]:
            result_array.append(array2[array2_idx])
            array2_idx += 1
        print(result_array)
    return result_array


result = merge(array_a, array_b)
print(result)

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1,2,3,5,40], [10,78,100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1,-1,0], [1, 6, 9, 10]))