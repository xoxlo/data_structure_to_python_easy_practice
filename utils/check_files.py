import os
def get_file_list_prac():
    file_list = [file for file in os.listdir("./PRACTICE/") if '.md' in file]
    file_list = sorted(file_list)
    return file_list
  
def make_info_prac(file_list):
    info = f"## PRACTICE\n\n"
    for file in file_list:
        temp = f"- [{file}](https://github.com/xoxlo/data_structure_to_python_easy_practice/tree/main/PRACTICE/{file})\n"
        info += temp
    return info

def get_file_list():
    file_list = [file for file in os.listdir("./Chapter_1/") if '.py' in file]
    file_list = sorted(file_list)
    return file_list
  
def make_info(file_list):
    info = f"## Chapter_01\n\n"
    for file in file_list:
        temp = f"- [{file}](https://github.com/xoxlo/data_structure_to_python_easy_practice/tree/main/Chapter_1/{file})\n"
        info += temp
    return info

def get_file_list2():
    file_list = [file for file in os.listdir("./Chapter_2/") if '.py' in file]
    file_list = sorted(file_list)
    return file_list
  
def make_info2(file_list):
    info = f"## Chapter_02\n\n"
    for file in file_list:
        temp = f"- [{file}](https://github.com/xoxlo/data_structure_to_python_easy_practice/tree/main/Chapter_2/{file})\n"
        info += temp
    return info

def get_file_list3():
    file_list = [file for file in os.listdir("./Chapter_3/") if '.py' in file]
    file_list = sorted(file_list)
    return file_list
  
def make_info3(file_list):
    info = f"## Chapter_03\n\n"
    for file in file_list:
        temp = f"- [{file}](https://github.com/xoxlo/data_structure_to_python_easy_practice/tree/main/Chapter_3/{file})\n"
        info += temp
    return info

def get_file_list4():
    file_list = [file for file in os.listdir("./Chapter_4/") if '.py' in file]
    file_list = sorted(file_list)
    return file_list
  
def make_info4(file_list):
    info = f"## Chapter_04\n\n"
    for file in file_list:
        temp = f"- [{file}](https://github.com/xoxlo/data_structure_to_python_easy_practice/tree/main/Chapter_4/{file})\n"
        info += temp
    return info

def get_file_list5():
    file_list = [file for file in os.listdir("./Chapter_5/") if '.py' in file]
    file_list = sorted(file_list)
    return file_list
  
def make_info5(file_list):
    info = f"## Chapter_05\n\n"
    for file in file_list:
        temp = f"- [{file}](https://github.com/xoxlo/data_structure_to_python_easy_practice/tree/main/Chapter_5/{file})\n"
        info += temp
    return info

def get_file_list6():
    file_list = [file for file in os.listdir("./Chapter_6/") if '.py' in file]
    file_list = sorted(file_list)
    return file_list
  
def make_info6(file_list):
    info = f"## Chapter_06\n\n"
    for file in file_list:
        temp = f"- [{file}](https://github.com/xoxlo/data_structure_to_python_easy_practice/tree/main/Chapter_6/{file})\n"
        info += temp
    return info

def get_file_list7():
    file_list = [file for file in os.listdir("./Chapter_7/") if '.py' in file]
    file_list = sorted(file_list)
    return file_list
  
def make_info7(file_list):
    info = f"## Chapter_07\n\n"
    for file in file_list:
        temp = f"- [{file}](https://github.com/xoxlo/data_structure_to_python_easy_practice/tree/main/Chapter_7/{file})\n"
        info += temp
    return info

def get_file_list8():
    file_list = [file for file in os.listdir("./Chapter_8/") if '.py' in file]
    file_list = sorted(file_list)
    return file_list
  
def make_info8(file_list):
    info = f"## Chapter_08\n\n"
    for file in file_list:
        temp = f"- [{file}](https://github.com/xoxlo/data_structure_to_python_easy_practice/tree/main/Chapter_8/{file})\n"
        info += temp
    return info

def get_file_list9():
    file_list = [file for file in os.listdir("./Chapter_9/") if '.py' in file]
    file_list = sorted(file_list)
    return file_list
  
def make_info9(file_list):
    info = f"## Chapter_09\n\n"
    for file in file_list:
        temp = f"- [{file}](https://github.com/xoxlo/data_structure_to_python_easy_practice/tree/main/Chapter_9/{file})\n"
        info += temp
    return info

def get_file_list10():
    file_list = [file for file in os.listdir("./Chapter_10/") if '.py' in file]
    file_list = sorted(file_list)
    return file_list
  
def make_info10(file_list):
    info = f"## Chapter_10\n\n"
    for file in file_list:
        temp = f"- [{file}](https://github.com/xoxlo/data_structure_to_python_easy_practice/tree/main/Chapter_10/{file})\n"
        info += temp
    return info

def get_file_list11():
    file_list = [file for file in os.listdir("./Chapter_11/") if '.py' in file]
    file_list = sorted(file_list)
    return file_list
  
def make_info11(file_list):
    info = f"## Chapter_11\n\n"
    for file in file_list:
        temp = f"- [{file}](https://github.com/xoxlo/data_structure_to_python_easy_practice/tree/main/Chapter_11/{file})\n"
        info += temp
    return info

def get_file_list12():
    file_list = [file for file in os.listdir("./Chapter_12/") if '.py' in file]
    file_list = sorted(file_list)
    return file_list
  
def make_info12(file_list):
    info = f"## Chapter_11\n\n"
    for file in file_list:
        temp = f"- [{file}](https://github.com/xoxlo/data_structure_to_python_easy_practice/tree/main/Chapter_12/{file})\n"
        info += temp
    return info

def make_read_me(info):
    return f"""
# 파이썬으로 쉽게 배우는 자료구조 (개정판)
<div align=center><h1>📚 STACKS</h1></div>
<div align=center> 
    <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
    <img src="https://img.shields.io/badge/java-007396?style=for-the-badge&logo=java&logoColor=white">
    <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
    <br>
</div>

> 책 표지

<img src="https://github.com/xoxlo/data_structure_to_python_easy_practice/assets/46445480/c4624456-228e-4d6a-a0d9-5c50ba664ee8" width="500" height="700"/>

각 챕터별 코드 실습 및 연습 문제 위주

{info}
"""


def update_readme():
    file_list_prac = get_file_list_prac()
    file_list = get_file_list()
    file_list2 = get_file_list2()
    file_list3 = get_file_list3()
    file_list4 = get_file_list4()
    file_list5 = get_file_list5()
    file_list6 = get_file_list6()
    file_list7 = get_file_list7()
    file_list8 = get_file_list8()
    file_list9 = get_file_list9()
    file_list10 = get_file_list10()
    file_list11 = get_file_list11()
    file_list12 = get_file_list12()
    info = make_info_prac(file_list_prac) + make_info(file_list) + make_info2(file_list2) + make_info3(file_list3) + make_info4(file_list4) + make_info5(file_list5) + \
            make_info6(file_list6) + make_info7(file_list7) + make_info8(file_list8) + make_info9(file_list9) + make_info10(file_list10) + make_info11(file_list11) + \
                make_info12(file_list12)
    readme = make_read_me(info)
    return readme


if __name__ == "__main__":
    readme = update_readme()
    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)
