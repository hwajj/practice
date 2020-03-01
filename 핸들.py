fname=input('파일이름입력하세요:')
try:
    fhand=open(fname)
except:
    print('파일명오류', fname)
    quit()
count=0
for line in fhand:
    if line.startswith('제목'):
        count=count+1
print(fname,'에는',count,'개의 제목이 있다')
