# 출석 번호 1,2,3,4 앞에 100을 붙여야함
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

#이름 길이로 변환
students = ["james", "jordan", 'curry']
print(students)
students = [len(j) for j in students]
print(students)

#대문자로 변환하기
students = ["james", "jordan", 'curry']
students = [i.upper() for i in students]
print(students)