# https://school.programmers.co.kr/learn/courses/30/lessons/172928
# 풀이일: 250924

def solution(park, routes):
    # 1. 지도 정보 배열화
    park_map = []
    pos = [0, 0]
    
    for idx, p in enumerate(park):
        park_line = list(p)
        if "S" in park_line:
            pos[0] = idx
            pos[1] = park_line.index("S")
        park_map.append(park_line)
    
    map_h = len(park_map)
    map_w = len(park_map[0])
    
    # park_map 검증
    print(park_map) 
    print(pos)
    print(map_h, map_w)
    
    # 2. 이동 알고리즘
    pos = [0, 0]
    for r in routes:
        moved_pos = pos[:]
        direction, distance = r.split()
        is_skip = False
        # 2-a. 경로 내 장애물 판단
        if direction == "N":
            for _ in range(int(distance)):
                moved_pos[0] -= 1
                if (moved_pos[0] < 0 or park_map[moved_pos[0], moved_pos[1]] == "X"):
                    is_skip = True
            # 2-b. 이동
            if is_skip:
                continue
            else:
                pos[0] -= distance
                # 2-a. 경로 내 장애물 판단
        if direction == "W":
            for _ in range(int(distance)):
                moved_pos[1] -= 1
                if (moved_pos[0] < 0 or park_map[moved_pos[0], moved_pos[1]] == "X"):
                    is_skip = True
            # 2-b. 이동
            if is_skip:
                continue
            else:
                pos[1] -= distance
                
        if direction == "S":
            for _ in range(int(distance)):
                moved_pos[1] -= 1
                if (moved_pos[0] < 0 or park_map[moved_pos[0], moved_pos[1]] == "X"):
                    is_skip = True
            # 2-b. 이동
            if is_skip:
                continue
            else:
                pos[1] -= distance
                
    
    # 3. 최종 위치 출력
    answer = []
    return answer

solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"])

# 아쉬운 점
# 1. 코드 반복 과다 -> dx, dy로 이동 정보 재활용 및 최종 이동 진행
# 2. 풀이 시간 과다 -> 꾸준히 문제 풀이 진행
# 3. 불필요한 코드 -> 지도 배열화 X
# 4. Python for-else 구문 공부