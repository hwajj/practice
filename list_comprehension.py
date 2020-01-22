#리스트 안에 for 문 포함하기

print('#a라는 리스트의 각 항목에 3을 곱한 결과를 result라는 리스트에 담는 예제', end=' ')
print('''
a=[1,2,3,4]
result=[]
for num in a:
    result.append(num*3)
print (result)
''')
a=[1,2,3,4]
result=[]
for num in a:
    result.append(num*3)
print (result)

print('\n\n#리스트 안에 for 문 포함하기', end='')
print('''
a=[1,2,3,4]
result=[num*3 for num in a]
print(result)
''')
a=[1,2,3,4]
result=[num*3 for num in a]
print(result)
