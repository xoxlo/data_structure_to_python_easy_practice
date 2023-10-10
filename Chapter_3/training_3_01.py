# 리스트의 데이터 : 전역 변수
capacity = 100
array = [None]*capacity
size = 0

# 리스트의 의 연산 : 일반 함수
def isEmpty():  # 공백 상태 검사
    if size == 0:
        return True
    else:
        return False

def isFull(): # 포화 상태 검사
    return size == capacity

# 공백상태와 포화상태를 왜 확인하는가?
# 공백 상태 : 데이터를 지우려고 하는데 데이터가 없다면 하나마나기 때문에
# 포화 상태 : 데이터를 추가하려고 하는데 꽉 차있다면 추가를 못하기 때문에

def getEntry(pos):
    if 0 <= pos < size :
        return array[pos]
    else : return None

def insert(pos, e):
    global size # size -> 전역변수
    if not isFull() and 0<=pos<=size:
        for i in range(size, pos,-1):
            array[i]=array[i-1]
        array[pos] = e
        size += 1
    else:
        print("리스트 overflow 또는 유효하지 않은 삽입 위치")
        exit()

def delete(pos):
    global size # size -> 전역변수
    if not isEmpty() and 0 <= pos < size:
        e = array[pos]
        for i in range(pos, size-1):
            array[i]=array[i+1]
        size -= 1
        return e
    else:
        print("리스트 underflow 또는 유호하지 않은 삭제 위치")
        exit()