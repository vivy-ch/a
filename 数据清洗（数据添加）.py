with open('output13.txt', 'r',encoding='utf-8') as f:
    lines = f.readlines()

with open('output14.txt', 'w',encoding='utf-8') as f:
    for line in lines:
        line = line.strip()  # 去掉行尾的换行符
        if line.endswith(':'):  # 如果行尾是冒号，说明没有数据
            line += '未搜索到对应企业'  # 在行尾添加文字
        f.write(line + '\n')  # 写回文件，加上换行符
