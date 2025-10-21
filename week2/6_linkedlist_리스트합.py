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


def get_linked_list_sum(linked_list_1, linked_list_2):
    list_1_string =""
    list_2_string =""

    list1_cur_node = linked_list_1.head
    list2_cur_node = linked_list_2.head

    while list1_cur_node.next is not None:
        list_1_string += f"{list1_cur_node.data}"
        list_2_string += f"{list2_cur_node.data}"

        list1_cur_node = list1_cur_node.next
        list2_cur_node = list2_cur_node.next
    
    list_1_string += f"{list1_cur_node.data}"
    list_2_string += f"{list2_cur_node.data}"

    
    return int(list_1_string) + int(list_2_string)


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))