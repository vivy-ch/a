with open('output11.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = [line.strip() + ';\n' for line in lines]

with open('output11.txt', 'w', encoding='utf-8') as f:
    for line in new_lines:
        f.write(line)
