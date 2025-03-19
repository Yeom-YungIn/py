def open_account():
    print("opening account function!!")

open_account()

balance = 0

def deposit(money):
    global balance
    balance = balance + money
    return balance

deposit(100)
print(balance)

def aaa(a):
    a += 1
    print(a)
    return a

b = aaa
b(10)
