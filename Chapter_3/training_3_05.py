from training_3_03 import *
# 배열구조의 리스트를 이용한 라인 편집기 프로그램

list = ArrayList()
while True:
    command = input("[메뉴선택] i-입력, d-삭제, r-변경, f-찾기, p-출력, l-파일읽기, s-저장, q-종료 => ")

    if command == 'i':
        pos = int(input(" 입력행 번호 : "))
        str = input(" 입력행 내용 : ")
        list.insert(pos,str)
        
    elif command == 'd':
        pos = int(input(" 삭제행 번호 : "))
        list.delete(pos)
    
    elif command == 'r':
        pos = int(input(" 변경행 번호 : "))
        str = input(" 변경행 내용 : ");
        list.replace(pos, str)
        
    elif command == 'p':
        print('Line Editor')
        for line in range(list.size):
            print('[%2d ] '%line, end='')
            print(list.getEntry(line))
        print()
        
    elif command == 'q': exit()
    
    elif command == 'l':
        filename = input("읽을 파일(확장자 포함)을 입력하세요 : ")
        infile = open(filename, "r")
        lines = infile.readlines()
        for line in lines:
            list.insert(list.size, line.rstrip('\n'))
        infile.close()
    
    elif command == 's':
        filename = input("저장할 파일(확장자 포함)을 입력하세요 : ")
        outfile = open(filename, "w")
        len = list.size
        for i in range(len):
            outfile.write(list.getEntry(i)+'\n')
        outfile.close()
        
    elif command == 'f':
        str = input('문자열을 입력해주세요 : ')
        for line in range(list.size):
            if str in list.getEntry(line):
                print('[%2d ] '%line, end='')
                print(list.getEntry(line))