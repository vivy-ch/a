import time
import random
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

# 创建一个WebDriver实例
webdriver_service = Service('C:/Users/ch/Desktop/app爬虫/edge驱动/msedgedriver.exe')
driver = webdriver.Edge(service=webdriver_service)

# 读取txt文件中的每一行
with open('numbers.txt', 'r') as f:
    numbers = f.readlines()

# 创建一个新的txt文件用于存储输出的数据
with open('output11.txt', 'w', encoding='utf-8') as f:
    for number in numbers:
        number = number.strip()  # 去掉每行的换行符
        url = f"https://cn.bing.com/search?q={number}"
        driver.get(url)

        # 等待JavaScript代码执行
        time.sleep(random.randint(1,1))

        try:
            # 使用find_elements方法获取所有的h3标签
            titles = driver.find_elements(By.CSS_SELECTOR, 'h2')
            # 使用切片操作获取前五个元素
            titles = titles[:5]
            if titles:
                # 创建一个列表用于存储所有的标题
                title_texts = []
                for title in titles:
                    title_texts.append(title.text)
                # 使用join方法将所有的标题连接成一个字符串，并写入文件
                f.write(f"{number}: {'; '.join(title_texts)}\n")
            else:
                f.write(f"{number}: 无\n")
        except NoSuchElementException:
            f.write(f"{number}: 无\n")

# 关闭WebDriver实例
driver.quit()











