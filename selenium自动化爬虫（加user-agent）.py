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

# 创建一个Options实例
options = Options()

# 设置User-Agent
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

driver = webdriver.Edge(service=webdriver_service, options=options)

# 读取txt文件中的每一行
with open('numbers.txt', 'r') as f:
    numbers = f.readlines()

# 创建一个新的txt文件用于存储输出的数据
with open('output.txt', 'w', encoding='utf-8') as f:
    for number in numbers:
        number = number.strip()  # 去掉每行的换行符
        url = f"https://haoma.baidu.com/phoneSearch?search={number}"
        driver.get(url)

        # 等待JavaScript代码执行
        time.sleep(random.randint(1,10))

        try:
            title = driver.find_element(By.CSS_SELECTOR, 'div.title')
            if title is not None:
                # 将数据写入txt文件
                f.write(f"{number}: {title.text}\n")
            else:
                f.write(f"{number}: 无\n")
        except NoSuchElementException:
            f.write(f"{number}: 无\n")
        input()
# 关闭WebDriver实例
driver.quit()









