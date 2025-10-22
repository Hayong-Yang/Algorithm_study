from collections import deque

# double_list = deque([6,7,8])
# double_list.rotate(2)
# second_last_num = double_list.popleft()
# print(second_last_num)

# def get_kth_node_from_last(list, k):
#     double_list = deque(list)
#     double_list.rotate(k)
#     kth_last_num = double_list.popleft()
#     return kth_last_num

# result = get_kth_node_from_last([6,7,8,9,10], 2)
# print(result)

# ______________

def get_kth_node_from_last(list, k):
    double_list = deque(list)
    kth_last_num = double_list[-k]
    return kth_last_num

result = get_kth_node_from_last([6,7,8,9,10], 2)
print(result)