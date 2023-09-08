import re

with open('output12.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    number, data = line.strip().split(':', 1)  # 只分割一次
    parts = data.split(';')
    new_parts = [part for part in parts if re.search('[\u4e00-\u9fa5]', part)]  # 如果部分中有中文
    new_data = ';'.join(new_parts)
    new_line = number + ':' + new_data + '\n'
    new_lines.append(new_line)

with open('output13.txt', 'w', encoding='utf-8') as f:
    for line in new_lines:
        f.write(line)
