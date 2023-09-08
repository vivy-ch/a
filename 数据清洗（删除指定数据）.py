import pandas as pd

with open('output13.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    number, data = line.split(':', 1)  # 只分割一次
    parts = data.split(';')
    new_parts = [part for part in parts if '哪的电话' not in part]
    new_data = ';'.join(new_parts)
    new_line = number + ':' + new_data
    new_lines.append(new_line)

with open('output13.txt', 'w', encoding='utf-8') as f:
    for line in new_lines:
        f.write(line)



