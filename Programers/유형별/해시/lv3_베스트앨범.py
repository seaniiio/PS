def solution(genres, plays):
    answer = []
    albums = {}
    for i in range(len(genres)):
        if genres[i] not in albums:
            albums[genres[i]] = [plays[i]]
            
            albums[genres[i]].append([[plays[i], i]]) # 형태 => 'pop' : [1100(장르의 총 재생수), [500, 1(고유번호)]]
        else:
            albums[genres[i]][0] = albums[genres[i]][0] + plays[i]
            albums[genres[i]].append([[plays[i], i]])
    print(list(albums.values()))
    albums = sorted(albums.values(), key=lambda x : x[0], reverse=True) # 노래 재생 기준으로 장르 정렬
    print(albums)
    
    for i in range(len(albums)): # 장르 개수만큼
        song_list = albums[i][1:]
        print(song_list)
        song_list_ordered = sorted(song_list, key=lambda x : x[0][0], reverse=True)
        answer.append(song_list_ordered[0][0][1])
        if len(song_list) > 1 : answer.append(song_list_ordered[1][0][1])
    return answer

'''
정렬을 잘 해야함
첫 번째는 장르를 정렬하는 것이고, 정렬 조건은 노래의 총 재생 횟수
두 번째는 각 장르에서 노래를 정렬하는 것이고, 정렬 조건은 노래별 재생 횟수
'''

# 시간 복잡도: O(n) + O(nlogn) (+ O(klogk))