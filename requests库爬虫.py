import requests
from bs4 import BeautifulSoup
import time
import random

# 读取txt文件中的每一行
with open('numbers.txt', 'r') as f:
    numbers = f.readlines()

# 创建一个新的txt文件用于存储输出的数据
with open('output1.txt', 'w', encoding='utf-8') as f:
    for number in numbers:
        number = number.strip()  # 去掉每行的换行符
        url = f"https://www.baidu.com/s?tn=44004473_8_oem_dg&ie=utf-8&wd={number}"

        # 使用requests库获取网页内容
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # # 等待一段时间
        # time.sleep(random.randint(1, 10))

        # 使用find_all方法获取所有的a标签
        titles = soup.find_all('a')
        if titles:
            for title in titles:
                # 将数据写入txt文件
                f.write(f"{number}: {title.text}\n")
        else:
            f.write(f"{number}: 无\n")


