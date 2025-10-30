"""
Q. 오늘 수업에 많은 학생들이 참여했습니다. 단 한 명의 학생을 제외하고는 모든 학생이 출석했습니다. 

모든 학생의 이름이 담긴 배열과 출석한 학생들의 배열이 주어질 때, 출석하지 않은 학생의 이름을 반환하시오
"""

all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

# 이 방법은 2중 for문 -> O(N^2)
# def get_absent_student(all_array, present_array):
#     absent_stu = "All present"
#     for student in all_array:
#         if student not in present_array:
#             absent_stu = student
#             return absent_stu
#     return absent_stu

# 딕셔너리를 통해 O(N)으로 해결 가능
def get_absent_student(all_array, present_array):
    stu_dict = {}
    for student in all_array:
        stu_dict[student] = True
    for present_stu in present_array:
        stu_dict.pop(present_stu,None)
    for absent_stu in stu_dict.keys():
        return absent_stu

print(get_absent_student(all_students, present_students))

print("정답 = 예지 / 현재 풀이 값 = ",get_absent_student(["류진","예지","채령","리아","유나"],["리아","류진","채령","유나"]))
print("정답 = RM / 현재 풀이 값 = ",get_absent_student(["정국","진","뷔","슈가","지민","RM"],["뷔","정국","지민","진","슈가"]))

"""
딕셔너리 메소드 정리

dict.keys()
dict.values()
dict.items()
dict["keys"] = values
dict.get("keys", None)
dict.pop("keys", None)
dict.popitem()
dict.update("keys":values)
dict.copy()
dict.clear()

| 메서드                             | 설명                          | 예시                                                        |
| ------------------------------- | --------------------------- | --------------------------------------------------------- |
| `dict.keys()`                   | 모든 키를 반환 (view 객체)          | `person.keys()` → `dict_keys(['name','age','job'])`       |
| `dict.values()`                 | 모든 값을 반환 (view 객체)          | `person.values()` → `dict_values(['하용',27,'developer'])`  |
| `dict.items()`                  | `(key, value)` 쌍을 튜플로 묶어 반환 | `person.items()` → `[('name','하용'), ('age',27)]`          |
| `dict.get(key, default)`        | 키가 없을 때 에러 대신 기본값 반환        | `person.get('email','없음')`                                |
| `dict.update({})`               | 딕셔너리 합치기 / 덮어쓰기             | `person.update({'age':28})`                               |
| `dict.pop(key)`                 | 해당 키를 제거하고 값 반환             | `person.pop('age')`                                       |
| `dict.popitem()`                | 마지막 (key, value) 쌍을 제거 후 반환 | `person.popitem()`                                        |
| `dict.clear()`                  | 모든 항목 삭제                    | `person.clear()`                                          |
| `dict.copy()`                   | 얕은 복사 (새 dict 생성)           | `copy_person = person.copy()`                             |
| `dict.setdefault(key, default)` | 키 없으면 추가, 있으면 무시            | `person.setdefault('country', 'Korea')`                   |
| `dict.fromkeys(keys, value)`    | 여러 키를 동일한 값으로 초기화           | `dict.fromkeys(['a','b','c'], 0)` → `{'a':0,'b':0,'c':0}` |

"""