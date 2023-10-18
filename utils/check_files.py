import os

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
        temp = f"- [{file}](https://github.com/xoxlo/data_structure_to_python_easy_practice/tree/main/Chapter_3/{file})\n"
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

각 챕터별 코드 실습이나 연습 문제 위주로 올립니다.

{info}
"""


def update_readme():
    file_list = get_file_list()
    file_list2 = get_file_list2()
    file_list3 = get_file_list3()
    file_list4 = get_file_list4()
    info = make_info(file_list) + make_info2(file_list2) + make_info3(file_list3) + make_info4(file_list4)
    readme = make_read_me(info)
    return readme


if __name__ == "__main__":
    readme = update_readme()
    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)
