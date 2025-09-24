def solution(players, callings):
    # 일단 리스트 내에서 앞뒤로만 자리 바꾸게 해보기
    # 시간초과 여부? -> 테스트 케이스 9번부터 시간초과 발생
#     for calling in callings:
#         front = players.index(calling) # front로 앞서나가는 사람
#         back = front - 1 # back으로 뒤처지게 된 사람
#         players[front], players[back] = players[back], players[front]
        
#     return players

    # 등수 기준 탐색? -> 탐색 시간 과다
    # 딕셔너리?와 리스트 병행? 딕셔너리 2개?
    ranking_name = {}
    ranking_num = {}
    
    for idx, p in enumerate(players):
        ranking_num[idx + 1] = p
        ranking_name[p] = idx + 1
    
    for back_name in callings:
        back_num = ranking_name[back_name]
        front_num = back_num - 1
        front_name = ranking_num[front_num]
        
        # 뒷사람 등수 감소
        ranking_name[back_name] -= 1
        ranking_num[back_num] = front_name
        # 앞사람 등수 증가
        ranking_name[front_name] += 1
        ranking_num[front_num] = back_name
    
    sort_list = sorted(ranking_name.items(), key = lambda x: x[1])
    return [x for x, y in sort_list]
    

# 풀이기법
#  - 딕셔너리 2개를 사용해 swap 해서 풀기

# 아쉬운점
#  - sorted 함수의 key 사용 미숙

# 추가 
#  - 찾는것만 딕셔너리로?
#  - 시간복잡도 계산해보기
#  - 다른 사람들 코드 이해해보기