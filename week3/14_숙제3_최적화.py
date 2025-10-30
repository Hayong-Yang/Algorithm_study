genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

from collections import defaultdict


# 장르 순서 구하기
# 장르별 -> (재생수, 인덱스) 리스트 구하기 -> 정렬[0:2]
def get_melon_best_album(genre_array, play_array):
    genre_dict = defaultdict(int) # 장르: 재생수 총합
    play_idx_dict = defaultdict(list) # 장르 : [(재생수,idx)]

    for idx, (genre, play) in enumerate(zip(genre_array, play_array)):
        genre_dict[genre] += play
        play_idx_dict[genre].append((play, idx))
    
    genre_sequence = sorted(genre_dict, key=genre_dict.get, reverse=True) # [1순위 장르, 2순위 장르...]

    answer = []
    for genre in genre_sequence:
        top2 = sorted(play_idx_dict[genre], key=lambda x: (-x[0], x[1]))[0:2] # 리스트에서 튜플을 하나씩 꺼내서, 튜플을 0내림차순 1 오름차순으로 정렬하고, 정렬된 top2만 골라온다
        answer.extend(idx for _, idx in top2)
    return answer


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))