from training_7_11 import hashFn # hashFn 모듈 불러오기
M = 13 # 해시 테이블의 크기
table = [None] * M # None으로 초기화

def search(key): # 해시 탐색
    i = hashFn(key) # 해시 함수 주소 계산
    count = M # 사이즈만큼 count
    while count > 0: # count가 0 이하될 때까지 반복, 즉 모든 해시 테이블의 위치를 탐색하는 것
        if table[i] == None : # 탐색 실패, 탐색 도중 None이 발견되면
            return None # None을 반환
        if table[i] == key : # 찾으려는 key에 맞는 레코드면?
            return table[i] # 그 위치에 있는 레코드 반환
        i = (i + 1) % M # 테이블의 크기로 나누어서 나머지를 구해 탐색 위치 설정
        count =- 1 
    
    return None # 다 돌았는데도 없으면 None
    