#while
customer = "손놈"
index = 5
while index >= 1:
    print("{0}, 가져가세요. {1} 번만 더 불러요.".format(customer, index))
    index -= 1
    if index == 0:
        print("끝")
