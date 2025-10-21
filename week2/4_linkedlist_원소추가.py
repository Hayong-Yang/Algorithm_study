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

    def print_all(self):
        cur = self.head
        all_node = ""
        while cur.next is not None:
            all_node += f"{cur.data} -> "
            cur = cur.next
        all_node += f"{cur.data}"
        print(all_node)

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        new_node = Node(value)

        if index ==0:
            new_node.next = self.head
            self.head = new_node
            return self.print_all()
        
        before_node = self.get_node(index-1)
        old_node = before_node.next
        before_node.next = new_node
        new_node.next = old_node
        
        return self.print_all()
    
linked_list = LinkedList(5)
linked_list.append(12)
linked_list.print_all()
linked_list.add_node(0, 3)
linked_list.add_node(2, 6)