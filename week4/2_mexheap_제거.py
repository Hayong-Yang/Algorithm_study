"""
Q. 맥스 힙은 원소를 제거한 다음에도 맥스 힙의 규칙을 유지해야 한다. 
맥스 힙의 원소를 제거하시오. 
"""
class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        last_idx = len(self.items) -1
        self.items[1], self.items[last_idx] = self.items[last_idx], self.items[1]
        # 루트 값 반환
        poped_value = self.items.pop()

        cur_idx = 1
        child_left_idx = cur_idx * 2
        child_right_idx = cur_idx * 2 + 1

        cur_value = self.items[cur_idx]
        child_left_value = self.items[child_left_idx]
        child_right_value = self.items[child_right_idx]

        while cur_value < child_left_value or cur_value < child_right_value or cur_idx != len(self.items)-1 :
            bigger_child_idx = 0
            if child_left_value > child_right_value:
                bigger_child_idx = child_left_idx
            elif child_left_value < child_right_value:
                bigger_child_idx = child_right_idx
            
            if cur_value < self.items[bigger_child_idx]:
                self.items[cur_idx], self.items[bigger_child_idx] = self.items[bigger_child_idx], self.items[cur_idx]
                cur_idx = bigger_child_idx
            else:
                break

        return poped_value


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]