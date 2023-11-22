from training_8_12 import * # 모스부호 관련 함수들 불러오기
morseCodetree = make_morse_tree() # 모스 부호 트리 노드 만드는 함수 선언
str = input("입력 문장 : ") # 사용자한테 모스부호로 바꿀 문장 입력 받음
mlist = [] # 모스부호를 저장할 리스트 선언
for ch in str: # str 하나하나씩 꺼내면서 반복
    code = encode(ch) # 문자 하나하나를 모스부호로 바꾸기 위해 인코딩
    mlist.append(code) # 변환된 부호를 리스트에 저장
print("모스 부호 : ",mlist) # 변환된 모스부호 출력
print("디코딩 : ",end='')
for code in mlist:
    ch = decode(morseCodetree, code)
    print(ch, end='') # 인코딩후 디코딩한 문장을 변환
print() # 여기서 디코딩된 문장과 입력 받은 문장을 비교해서 정확하게 됐는지 확인