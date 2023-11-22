from training_8_14 import heappush # 힙 삽입 연산 불러오기
from training_8_15 import heappop # 힙 삭제 연산 불러오기

def make_tree(freq):
    heap = [0]
    for n in freq:
        heappush(heap, n)
        
    for i in range(1, len(freq)):
        e1 = heappop(heap)
        e2 = heappop(heap)
        heappush(heap, e1 + e2)
        print(" (%d + %d)" % (e1, e2))
        
label = ['E', 'T', 'N', 'I', 'S']
freq = [15, 12, 8, 6, 4]
make_tree(freq)