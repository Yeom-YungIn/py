absent = [2,5]
no_book = [7]
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_book:
        print("{0} 책을 안가져와?".format(student))
        break
    print("{0}, 안녕".format(student))