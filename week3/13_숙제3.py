# Q3. ✍️ 멜론 베스트 앨범 뽑기 
"""
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

제한사항
genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다.
"""
# 1. 장르별 전체 재생 수 구하기 -> 먼저 올 장르 결정
# -> 장르별 최대 2곡 수록 가능
# -> 장르끼리 재생횟수 같으면 인덱스가 낮은 곡 먼저 수록
# 2. 해당 장르 다 수록했으면 다음 장르로 넘어가기 

# 딕셔너리 -> "장르": [곡 인덱스 순서 배열]

"""
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
# 정답 = [4, 1, 3, 0]
"""


def get_melon_best_album(genre_array, play_array):
    sequence_dict = {}
    for idx, (genre, num) in enumerate(zip(genre_array, play_array)):
        if genre not in sequence_dict:
            sequence_dict[genre] = [0,[]]
        sequence_dict[genre][0] += num
        sequence_dict[genre][1].append({f"{idx}": num})
    sorted_dict = dict(sorted(sequence_dict.items(), key= lambda x: x[1][0], reverse=True))
    sorted_genre_list = sorted_dict.keys()
    
    # print(sorted_dict)        
    # print(sorted_genre_list)   

    final_answer = []
    for genre in sorted_genre_list:
        song_list = sorted_dict[genre][1]  # 리스트
        song_dict = {}
        for d in song_list:
            song_dict.update(d)
        sorted_song  = sorted(song_dict.items(), key = lambda x: (-x[1], x[0]))
        final_answer.extend([int(idx) for idx, _ in sorted_song[:2]])
    return final_answer


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))


"""
from collections import defaultdict

def get_melon_best_album(genres, plays):
    total = defaultdict(int)        # 장르별 총 재생수
    bucket = defaultdict(list)      # 장르별 곡 목록: [(play, idx), ...]

    for i, (g, p) in enumerate(zip(genres, plays)):
        total[g] += p
        bucket[g].append((p, i))    # idx를 문자열로 만들 필요 없음

    # 장르를 총 재생수 내림차순으로 정렬
    order = sorted(total, key=total.get, reverse=True)

    answer = []
    for g in order:
        # 장르 내 정렬: 재생수 내림차순, 같으면 idx 오름차순
        top2 = sorted(bucket[g], key=lambda x: (-x[0], x[1]))[:2]
        answer.extend(i for _, i in top2)
    return answer
"""