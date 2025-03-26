gun = 10

def checkpoint(soldiers):
    global gun # 함수 외부의 변수를 사용 가능
    gun = gun - soldiers
    return gun


print(checkpoint(1))