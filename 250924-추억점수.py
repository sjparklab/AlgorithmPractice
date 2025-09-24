from collections import defaultdict

def solution(name, yearning, photo):
    answer = []
    # name - yearning 딕셔너리화 진행
    # 문제 조건 상 name 중복 X
    score_dict = defaultdict(int)
    for n, score in zip(name, yearning):
        score_dict[n] = score
    
    for p in photo:
        score = 0
        for person in p:
            score += score_dict[person]
        answer.append(score)
    
    return answer

# 풀이기법
#  - 딕셔너리에 담아서 key-value로 바로 접근하기

# 아쉬운점
#  - defaultdict()의 from collections import defaultdict 암기 필요

# 추가
#  - 일반 딕셔너리만 사용하려면 반드시 in 문법으로 동작 필요한지 확인