import os

def get_file_list():
    file_list = [file for file in os.listdir("./Chapter_1/") if "1" in file]
    file_list = sorted(file_list)
    total_file_cnt = len(file_list)
    return file_list, total_file_cnt
  
  
def make_info(file_list, total_file_cnt):
    info = f"## Chapter_01\nTotal Practice Count: {total_file_cnt}개\n"
    for file in file_list:
        temp = f"- [{file}](https://github.com/xoxlo/data_structure_to_python_easy_practice/tree/main/Chapter_1/{file})\n"
        info += temp
    return info
    

def make_read_me(info):
    return f"""# 파이썬으로 쉽게 배우는 자료구조 (개정판)
>
> 책 표지
<img src="https://github.com/xoxlo/data_structure_to_python_easy_practice/assets/46445480/c4624456-228e-4d6a-a0d9-5c50ba664ee8" width="500" height="700"/>

각 챕터별 코드 실습이나 연습 문제 위주로 올립니다.

{info}
## Chapter_02
## Chapter_03
## Chapter_04
## Chapter_05
## Chapter_06
## Chapter_07
## Chapter_08
## Chapter_09
## Chapter_10
## Chapter_11
## Chapter_12
"""


def update_readme():
    file_list, total_file_cnt = get_file_list()
    info = make_info(file_list, total_file_cnt)
    readme = make_read_me(info)
    return readme


if __name__ == "__main__":
    readme = update_readme()
    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)
