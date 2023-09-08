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

driver.delete_all_cookies()

# 创建一个新的txt文件用于存储输出的数据
with open('output.txt', 'w', encoding='utf-8') as f:
    for number in numbers:
        number = number.strip()  # 去掉每行的换行符
        url = f"https://haoma.baidu.com/phoneSearch?search={number}"
        driver.get(url)

        # 添加cookie
        cookie_str = 'BIDUPSID=A52410D40976720B2873BD8474D47AAB; PSTM=1691493160; BAIDUID=A52410D40976720B747A676C0714EC99:FG=1; __sec_t_key=61c98628-40be-4d74-b525-c815507b5fed; Hm_lvt_71927aaa06a0dc9d2d16f927f1f6937f=1693817787; BDUSS=0lscTI0OEhkaEpzbmFvRGVhdnBqbXJqOE43SWU1cUxobFpFenFpUU4wbmJLQjFsSUFBQUFBJCQAAAAAAAAAAAEAAABt4mJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANub9WTbm~Vkb; BDUSS_BFESS=0lscTI0OEhkaEpzbmFvRGVhdnBqbXJqOE43SWU1cUxobFpFenFpUU4wbmJLQjFsSUFBQUFBJCQAAAAAAAAAAAEAAABt4mJOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANub9WTbm~Vkb; delPer=0; PSINO=6; BAIDUID_BFESS=A52410D40976720B747A676C0714EC99:FG=1; ZFY=34u1ajNU:B5EFlhOmfF1Rbq0ZLPnlBvtbhgco33TGWAA:C; Hmery-Time=3902565072; BDRCVFR[paU0ukvnltR]=I67x6TjHwwYf0; ZD_ENTRY=baidu; BDRCVFR[kSyA9a8U-kc]=mk3SLVN4HKm; BDRCVFR[BR_gAgb7m16]=mbxnW11j9Dfmh7GuZR8mvqV; __bid_n=18a5f9052252304b42bd07; H_PS_PSSID=26350; BCLID=12307317178942135122; BCLID_BFESS=12307317178942135122; BDSFRCVID=XsIOJeC62rxWgU3fnAAvukQXne3bwA6TH6aoR7XoJizsv94ytbq_EG0PgU8g0KuMlEnIogKKKmOTH1AF_2uxOjjg8UtVJeC6EG0Ptf8g0x5; BDSFRCVID_BFESS=XsIOJeC62rxWgU3fnAAvukQXne3bwA6TH6aoR7XoJizsv94ytbq_EG0PgU8g0KuMlEnIogKKKmOTH1AF_2uxOjjg8UtVJeC6EG0Ptf8g0x5; H_BDCLCKID_SF=JJu8oIPXtKvbfP0k5-oSbttehH8X5-Cst2cJ2hcH0KLKVRoe0qAbb4Cyhhbtahovae-j5tO8KMb1MlnNDhjI3RL1LxbhtJ5HLeONbl5TtUJtSDnTDMRhqfA0QUJyKMniWKj9-pPh0lQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuj5L2D6bBjN8s54JJ26c0LPI82P5Hfn5Y-Pvo5t3H-UnLq-uetgOZ0l8KtDIMsUODK4j_KU-e5fRIXP6-tjryKUomWIQHDpc8X4OaqJ043GQe2PR7QDT4KKJxQPPWeIJo5fcsX4CwhUJiBMnLBan7oljIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbC_lDTKhjjvyepOhetJeHjQaBjrJabC3SlumXU6qLT5XLPjKybv95Doe3K3a2MjiDR53btvchl0njxQyhROuMRAD34cu5f3xoJcybfonDh8RbG7MJUntKHvaopTO5hvvOn6O3MAaLfKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQbG_EJ5FDJbC8oK8Qb-3bK4bGh4JqbDCShUFsbb0OB2Q-5KL-JMj0fJ6Pb4T5-PP0MnQv2tRbK2FH_MbdJJjoMCO3-jQf5h30Kt7RJhok-mTxoUJP5DnJhhvqXJu2DPuebPRiB-r9Qg-D5lQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0M5DK0MKIRDjtBj6bMbMkXb43B2ICX3buQyPOz8pcNLTDKKRkibn_eKt6C06ctBMj9aJK5H43qjlO1j4_e0GJv2MT0Mj7qVCbXbnoa_p5jDh3J3jksD-RtW474ae5y0hvcWb6cShPlLfjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t225Qh-p52f60fJbuq3H; H_BDCLCKID_SF_BFESS=JJu8oIPXtKvbfP0k5-oSbttehH8X5-Cst2cJ2hcH0KLKVRoe0qAbb4Cyhhbtahovae-j5tO8KMb1MlnNDhjI3RL1LxbhtJ5HLeONbl5TtUJtSDnTDMRhqfA0QUJyKMniWKj9-pPh0lQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuj5L2D6bBjN8s54JJ26c0LPI82P5Hfn5Y-Pvo5t3H-UnLq-uetgOZ0l8KtDIMsUODK4j_KU-e5fRIXP6-tjryKUomWIQHDpc8X4OaqJ043GQe2PR7QDT4KKJxQPPWeIJo5fcsX4CwhUJiBMnLBan7oljIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbC_lDTKhjjvyepOhetJeHjQaBjrJabC3SlumXU6qLT5XLPjKybv95Doe3K3a2MjiDR53btvchl0njxQyhROuMRAD34cu5f3xoJcybfonDh8RbG7MJUntKHvaopTO5hvvOn6O3MAaLfKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQbG_EJ5FDJbC8oK8Qb-3bK4bGh4JqbDCShUFsbb0OB2Q-5KL-JMj0fJ6Pb4T5-PP0MnQv2tRbK2FH_MbdJJjoMCO3-jQf5h30Kt7RJhok-mTxoUJP5DnJhhvqXJu2DPuebPRiB-r9Qg-D5lQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0M5DK0MKIRDjtBj6bMbMkXb43B2ICX3buQyPOz8pcNLTDKKRkibn_eKt6C06ctBMj9aJK5H43qjlO1j4_e0GJv2MT0Mj7qVCbXbnoa_p5jDh3J3jksD-RtW474ae5y0hvcWb6cShPlLfjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t225Qh-p52f60fJbuq3H; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BMAP_SECKEY=CFllOUQ3Q1SfFwyXjReIW6PXo-_Xcwdkiboqkb7RN6qKpeT2uKzuhshlv3AY9ARbffmIq79jlv2AyI-uzSGJOzax67lHj0kvHZNwcyutrSr4OccYXzPZvMJFU0TSvXFzTAIz_RZrtB46SvIRK_ZM1t9In7D1Djc984qFNjiBC8DBWZy5BNRvV2QWFyDjDeHN; RT="z=1&dm=baidu.com&si=1b308106-6a7e-4409-a699-f11bbc86db46&ss=lm73bv9d&sl=1&tt=2hl&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf"; Hm_lpvt_71927aaa06a0dc9d2d16f927f1f6937f=1693966848; SECKEY_ABVK=CFllOUQ3Q1SfFwyXjReIW/0fIzJK5lPyu6d1L2IuVfM%3D; ab_sr=1.0.1_NGNmZjk2ZDEwZTA1M2U2MTFhOTc3M2E3YTY5MWMzYThkN2FjNWI1M2IzZDg2OGQ4MjYyNjc2YTY4ODkwMmEwMzk1Mzc5M2NjMjA1M2FhMmY1MzM4ODEyMzQ4OTljMjg0OTQ4NmU5Y2VmYzdlMGQ1MmFmNGIyNzViYWQxOTEwNzg0ZGY4ZTI2ODdmZTcwMDcyM2FiNzlhZjMxYTNlNTMwMg=='
        for line in cookie_str.split(';'):
            name, value = line.strip().split('=', 1)
            cookie = {'name': name, 'value': value}
            driver.add_cookie(cookie)

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

