class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self,value):
        self.head = Node(value)
    
    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        all_node = []
        while cur.next is not None:
            all_node.append(cur.data)
            cur = cur.next
        all_node.append(cur.data)
        print(all_node)

    def get_node(self, index):
        cur = self.head
        if index == 0:
            return cur.data
        else:
            for i in range(index):
                cur = cur.next
            return cur.data
        

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(30)
linked_list.append(3)
print(linked_list.get_node(0)) # -> 5를 들고 있는 노드를 반환해야 합니다!
print(linked_list.get_node(1)) 
print(linked_list.get_node(2)) 
print(linked_list.get_node(3)) 
linked_list.print_all()
