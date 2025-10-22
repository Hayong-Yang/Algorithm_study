# 무작위 수 찾기
# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 2이 존재한다면 True 존재하지 않는다면 False 를 반환하시오.

# [0, 3, 5, 6, 1, 2, 4]

finding_target = 1
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

class Binary_search:
    def __init__(self, target, array):
        self.target = target
        self.array = array
        self.cur_min_idx = 0
        self.cur_max_idx = len(self.array) -1
        self.cur_guess_idx = (self.cur_min_idx + self.cur_max_idx) // 2
    def high_search(self):
        # 초기화
        self.cur_min_idx = 0
        self.cur_max_idx = len(self.array) -1
        self.cur_guess_idx = (self.cur_min_idx + self.cur_max_idx) // 2

        while self.cur_min_idx <= self.cur_max_idx:
            if self.array[self.cur_guess_idx] == self.target:
                return True
            else:
                self.cur_min_idx = self.cur_guess_idx + 1
                self.cur_guess_idx = (self.cur_min_idx + self.cur_max_idx) // 2
        return False
    def low_search(self):
        # 초기화
        self.cur_min_idx = 0
        self.cur_max_idx = len(self.array) -1
        self.cur_guess_idx = (self.cur_min_idx + self.cur_max_idx) // 2

        while self.cur_min_idx <= self.cur_max_idx:
            if self.array[self.cur_guess_idx] == self.target:
                return True
            else:
                self.cur_max_idx = self.cur_guess_idx - 1
                self.cur_guess_idx = (self.cur_min_idx + self.cur_max_idx) // 2
        return False

def is_exist_target_number_binary(target, array):
    tool = Binary_search(target, array)
    high_result = tool.high_search()
    low_result = tool.low_search()

    if high_result == True or low_result == True:
        return True 

    return False

result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)