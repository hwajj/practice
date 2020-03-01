fhand=open('핸들.txt')
for line in fhand:
    line.rstrip()
    if not line.startswith('내용'):
        continue
    print(line)
