from training_7_11 import hashFn
M = 13
table = [None] * M
def insert(key):
    i = hashFn(key) # 해시 주소 계산
    count = M # table 사이즈 만큼 count 지정
    while count > 0: # count가 0 이상일 때 계속 반복
        
        if table[i] == None: # 넣으려고 하는 주소가 비어있다면
            break # while문 탈출
        
        i = (i + 1) % M 
        count -= 1
        
    if count > 0: # count가 0 이상이면
        table[i] = key # key값을 table에 삽입