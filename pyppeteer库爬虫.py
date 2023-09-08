import asyncio
from pyppeteer import launch

async def get_title(number):
    browser = await launch(args=['--proxy-server=111.72.197.71:4256'])
    page = await browser.newPage()
    url = f"https://haoma.baidu.com/phoneSearch?search={number}"
    response = await page.goto(url)
    if response.status != 200:
        print(f"Failed to load {url}, status code: {response.status}")
        return "错误"
    try:
        title_element = await page.querySelector('div.title')
        title = await page.evaluate('(element) =&gt; element.textContent', title_element)
    except Exception as e:
        title = "无"
    await browser.close()
    return title

# 读取txt文件中的每一行
with open('numbers.txt', 'r') as f:
    numbers = f.readlines()

# 创建一个新的txt文件用于存储输出的数据
with open('output.txt', 'w', encoding='utf-8') as f:
    for number in numbers:
        number = number.strip()  # 去掉每行的换行符
        title = asyncio.get_event_loop().run_until_complete(get_title(number))
        f.write(f"{number}: {title}\n")


