# Q. 링크드 리스트의 끝에서 K번째 값을 반환하시오.
'''
[6] -> [7] -> [8] # 이런 링크드 리스트가 입력되었을 때, 
                  # 끝에서 2번째 값은 7을 반환해야 합니다!

1234
123456 길이 6일때 끝에서 2번째는 index = 6-2

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        cur = self.head
        cur_index = 0
        while cur.next is not None:
            cur_index += 1
            cur = cur.next

        target_index = (cur_index+1) - k

        cur = self.head
        cur_index = 0
        while cur_index != target_index:
            cur_index += 1
            cur = cur.next

        return cur


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!