class Node:
    def __init__(self,data):
        self.data = data
        self.next = None # 다음 노드의 주소를 담음

first_node = Node(5)
second_node = Node(10)
first_node.next = second_node
print(first_node.next.data)

