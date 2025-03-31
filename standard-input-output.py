import sys

print("python","java",sep=" & ", end=" ? ")
print("표준 출력", file=sys.stdout)
print("표준 에러", file=sys.stderr)


scores = {"수학" : 100, "영어" : 80, "국어" : 90}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

for num in range(10):
      print(str(num).zfill(3))


answer = input("값 입력")

print(answer)