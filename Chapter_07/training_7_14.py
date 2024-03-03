from training_7_12 import hashFn
M = 13
table = [None] * M

def delete(key) :
    i = hashFn(key) # 해시 주소 계산
    count = M
    while count > 0:
        if table[i] == key : # 삭제할 위치 발견 : i
            table[i] = -1 # -1 저장, 사용되었다가 삭제된 경우를 뜻함
            return 
        if table[i] == None : # None은 테이블에 삭제할 
            return
        i = (i + 1) % M # 다음 조사 위치
        count -= 1