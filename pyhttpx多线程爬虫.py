import pyhttpx
import json

# 读取txt文件中的每一行
with open('numbers.txt', 'r') as f:
    numbers = f.readlines()

# 创建一个新的txt文件用于存储输出的数据
with open('output.txt', 'w', encoding='utf-8') as f:
    for number in numbers:
        number = number.strip()  # 去掉每行的换行符
        url = f"https://haoma.baidu.com/phoneSearch?search={number}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        }
        session = pyhttpx.HttpSession()  # 注意：使用多线程时，这个设置成局部变量
        res = session.get(url=url, headers=headers)

        try:
            data = json.loads(res.text)
            title = data.get('title')
            if title is not None:
                # 将数据写入txt文件
                f.write(f"{number}: {title}\n")
            else:
                f.write(f"{number}: 无\n")
        except json.JSONDecodeError:
            f.write(f"{number}: 无\n")

