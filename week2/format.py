class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self,value):
        self.head = Node(value)
    
    def append(self,value):
        cur = self.head

        while cur.next is not None:
            cur = cur.next
        
        cur.next = Node(value) 
    
    def print_all(self):
        cur = self.head
        all_node = ""
        while cur.next is not None:
            all_node += f"{cur.data} -> "
            cur = cur.next
        all_node += f"{cur.data}"
        print(all_node)
