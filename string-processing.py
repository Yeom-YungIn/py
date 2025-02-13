sentence = '파이썬을 공부합니다.'
print(sentence)
sentence = '파이썬은 쉬워요.'
print(sentence)
sentence = """
파이썬은 변수에 값을 재할당 할 수 있나봐요.
"""
print(sentence)


#Slicing
registerNum = '100101-1010111'

findZero = registerNum.find('0')
print(findZero)

print('7번째: ' + registerNum[7])
print('뒤 7개: ' + registerNum[7:])
print('뒤부터 7개: ' + registerNum[-7:])


python = 'Python is Easy'
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace('Python', 'JS'))

index = python.index('y')
print(index)
index = python.index('y', index + 1)
print(index)

print(python.find('JS'))
# print(python.index('JS')) 인덱스는 에러
print(python.find('P'))


# 문자열 포멧
print("a" + "b")

print('%d + %d  = %d' % (1, 2, 3))
print("파이썬은 %s" % '쉽다')
print("학점 %c" % 'A')

print('나는 {} 입니다.'.format(3))
print('{} + {}  = {}'.format(1,2,3))

#탈출문자
print('안녕\n하세요')
print('안녕 "하세"요')
print('안녕 \"하세\"요')

#\\ => \
print("\\")

#\r 커서를 맨 앞으로
print("red\rpine Apple")

# \b 백스페이스
print('12345\b789')

#\t tab
print('124\t\t\t456')