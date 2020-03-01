count=dict()
print('문장을 입력하시면 문장안에 단어 분포를 분석해 드려요:')
line=input('')
words=line.split()
for word in words:
    count[word]=count.get(word,0)+1
print(count)
