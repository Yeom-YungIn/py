# 리스트 []

subway = [10, 20, 30]

print(subway.index(10))

subway.append(40)
print(subway)

subway.insert(0, 0)
print(subway)

subway.pop()
print(subway)

subway.reverse()
print(subway)

subway.insert(0, 10)
print(subway.count(10))

subway.sort()

subway.clear()
print(subway)

subway.append(20)
subway.append('안녕')
subway.append('A')
print(subway)
