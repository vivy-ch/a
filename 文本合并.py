data_dict = {}

# 读取并处理第一个文件
with open('output10.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        number, data = line.strip().split(':', 1)  # 只分割一次
        if number in data_dict:
            data_dict[number] += ';' + data
        else:
            data_dict[number] = data

# 读取并处理第二个文件
with open('output11.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        number, data = line.strip().split(':', 1)  # 只分割一次
        if number in data_dict:
            data_dict[number] += ';' + data
        else:
            data_dict[number] = data

# 将合并后的数据写入到新的文件中
with open('output12.txt', 'w', encoding='utf-8') as f:
    for number, data in data_dict.items():
        f.write(number + ':' + data + '\n')

