#구구단 print 들여쓰기 위치에 따라 배열이 다름

print('''1.print(\'\')가 for문 안에,end=\'\'가 다음줄로 넘기지 않게'
for i in range(2,5):
    for j in range(1,10):
        print(i*j, end=' ')
        print('')
    ''')
for i in range(2,5):
    for j in range(1,10):
        print(i*j, end=" ")
        print('')

print('''\n 2.for j안에 print(\'\') 있으므 j끝나기전에 i*j연산 끝날때마다 줄바꿈
for i in range(2,5):
    for j in range(1,10):
        print(i*j)
        print('')
    ''')
for i in range(2,5):
    for j in range(1,10):
        print(i*j)
        print('')


print('''\n 3.print('')가 for j 문 밖에, j 끝날때 줄바꾸기)
for i in range(2,5):
    for j in range(1,10):
        print(i*j, end=" ")
    print('')''')

for i in range(2,5):
    for j in range(1,10):
        print(i*j, end=" ")
    print('')


print('''\n 4.j를 한차례 돌고나면 for i 들어가기 전에 print('')가 한줄 띔
for i in range(2,5):
    for j in range(1,10):
        print(i*j)
    print('') ''')
for i in range(2,5):
    for j in range(1,10):
        print(i*j)
    print('')

print('''\n 5.print(\'\')가 바깥에 ~ for i까지 다 끝나고 나서 한칸띔
for i in range(2,5):
    for j in range(1,10):
        print(i*j)
print('')
''')

for i in range(2,5):
    for j in range(1,10):
        print(i*j)
print('')
