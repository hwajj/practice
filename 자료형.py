print(' \n 1.리스트 \n a=[0,1,2,3]')

a=[0,1,2,3]

print('''
>>>str(a[2])+hi >>>3hi
>>a.append([4,5])
>>>a.append(4) >>>append는 하나씩 붙이기
>>>a.sort()
>>>a.reverse() 
>>>a.index() >>>위치값을 리턴
>>>a.insert(0,44)>>0번째에 44 삽입
>>>a.remove(0,1) >>>첫번째로 나오는 1 삭제
''')


print('\n 2. 튜플 - 튜플의 항목값은 변화 불가 ~ insert, append 안됨,t1=(), 괄호 생략가능')
print('''0=()
t1=(1,)
t2=(1)
t3=(1,2)
t4=1,2
t5=('a','b',('ab','cd')) \n

print(t0)
print(t1)
print(t2) >>>(콤마)를 사용하지 않는 경우 튜플로 선언되지 않아 연산안됨
print(t3)
print(t0+t1)
print(t1+t4)
print(t1+t5)
print(t2+t3) >>>TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
print(t2+t4) >>>TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
print(t2+t5) >>>TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
print(t3+t4)
print(t3+t5)
print(t4+t5) >>>t3=t4, ()생략가능  \n ''' )

t0=()
t1=(1,)
t2=(1)
t3=(1,2)
t4=1,2
t5=('a','b',('ab','cd'))

print(t0)
print(t1)
print(t2)
print(t3)
print(t0+t1)
print(t1+t4)
print(t1+t5)
#print(t2+t3)
#print(t2+t4)
#print(t2+t5)
print(t3+t4)
print(t3+t5)
print(t4+t5)


print('''\n 3.딕셔너리자료형
      dic={'이름':'현아','번호':'01033323413','생일':'1114' }
      >>>dic['이름'] #현아 출력
      >>>dic['취미']='서핑' #딕셔너리쌍 추가''')

dic={'이름':'현아','번호':'01033323413','생일':'1114' }


