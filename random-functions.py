from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값
print(random() * 10)
print(random() * 100)
print(random() * 1000)
print(random() * 10000)

print(int(random() * 45) + 1) # 1부터 45 이하의 랜덤한 정수

print(randrange(1,100))# 1부터 100 미만의 랜덤한 정수