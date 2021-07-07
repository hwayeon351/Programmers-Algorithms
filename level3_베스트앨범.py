from collections import defaultdict, Counter
def solution(genres, plays):
    answer = []
    genres_plays_dict = defaultdict(list)
    num_play_genres = Counter()
    
    for i in range(len(genres)):
        genres_plays_dict[genres[i]].append([plays[i], i])
        num_play_genres[genres[i]] += plays[i]
        
    for key, val in list(genres_plays_dict.items()):
        genres_plays_dict[key] = sorted(val, key = lambda x:(-x[0],x[1]))
        
    for g, n in num_play_genres.most_common():
        song = genres_plays_dict[g]
        if len(song) == 1:
            answer.append(song[0][1])
            continue
        for j in range(2):
            answer.append(song[j][1])
            
    return answer
