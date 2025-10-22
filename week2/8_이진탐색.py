finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    cur_min_idx = 0
    cur_max_idx = len(array) -1
    cur_guess_idx = (cur_min_idx + cur_max_idx) // 2

    cycle_count = 0

    while cur_min_idx <= cur_max_idx:
        if array[cur_guess_idx] == target:
            return True, cur_guess_idx, cycle_count+1
        elif array[cur_guess_idx] < target:
            cur_min_idx = cur_guess_idx + 1
        elif array[cur_guess_idx] > target:
            cur_max_idx = cur_guess_idx -1
        cur_guess_idx = (cur_min_idx + cur_max_idx ) // 2
        cycle_count += 1            

    return False, cycle_count

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)