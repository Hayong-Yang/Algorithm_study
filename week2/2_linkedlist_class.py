class Node:
    def __init__(self,data):
        self.data = data
        self.next = None # 다음 노드의 주소를 담음

class LinkedList:
    def __init__(self,value):
        self.head = Node(value)
    
    def append(self,value):
        cur = self.head

        while cur.next is not None:
            cur = cur.next
        
        cur.next = Node(value) # 끝에가 None인 노드(즉, 마지막 노드)에 next에 새로운 노드 추가
    
    def print_all(self):
        # cur = self.head
        # all_node = []
        # while cur.next is not None:
        #     all_node.append(cur.data)
        #     cur = cur.next
        # all_node.append(cur.data)
        # print(all_node)

        cur = self.head
        all_node = ""
        while cur.next is not None:
            all_node += f"{cur.data} -> "
            cur = cur.next
        all_node += f"{cur.data}"
        print(all_node)


# linked_list = LinkedList(5)
# print(linked_list.head.data)
# print(linked_list.head.next)

# linked_list.append(10)
# print(linked_list.head.data)
# print(linked_list.head.next.data)


linked_list = LinkedList(5)
linked_list.print_all()
linked_list.append(10)
linked_list.print_all()
linked_list.append(15)
linked_list.print_all()
linked_list.append(20)
linked_list.print_all()