#구구단 print 들여쓰기 위치에 따라 배열이 다름

print('매번 줄바꿈')
for i in range(2,5):
    for j in range(1,10):
        print(i*j, end=" ") #end('')는 해당결과값 출력시 다음줄로 넘기지 않게함
        print('') #print('')가 for문 안에 있으니까  2*1 다음줄에 2*2

print('')
print('end 없이 줄바꿈')
for i in range(2,5):
    for j in range(1,10):
        print(i*j) #end가 없어서 i*j끝날때마다 줄바꿈
        print('') #줄바꿈했는데 한줄을 띔

print('')

print('2단 끝나면 줄바꿈')
for i in range(2,5):
    for j in range(1,10):
        print(i*j, end=" ") 
    print('') #print('')가 for밖에 있으니까 2단이 끝난 후에 줄바꿈

print('')

print('단이 바뀔때 한줄 띔')
for i in range(2,5):
    for j in range(1,10):
        print(i*j) #2*1 , 2*2 를 for로 반복함 근데 아무말 없으니까 한줄에 한칸씩
    print('') #i 2일때 두번째 for로 들어가서 j를 1~9까지 반복하고 나면 print('')한줄 띄어주고 i 3으로.. 

print('')
print('''
2
4
6
8
10
3
6
9
하고 나중에 맨마지막에 한줄 공백
''')

for i in range(2,5):
    for j in range(1,10):
        print(i*j) #2*1 하고 한칸씩 더 띄우고 엔터
print('')

