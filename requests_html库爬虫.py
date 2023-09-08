from requests_html import HTMLSession

session = HTMLSession()
url = "https://haoma.baidu.com/phoneSearch?search=8008205035"
response = session.get(url)

# 使用JavaScript渲染页面
response.html.render()

title = response.html.find('a', first=True)


print(title.text)





