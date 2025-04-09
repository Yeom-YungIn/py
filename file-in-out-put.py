from typing import TextIO

# score_file: TextIO = open("score.txt", "w", encoding="utf-8")
# print("수학: 0", file=score_file)
# print("영어: 100",file=score_file)
# score_file.close()

# score_file: TextIO = open("score.txt", "a", encoding="utf-8")
# score_file.write("HELLO.")
# score_file.close()

# score_file:TextIO = open("score.txt","r", encoding="utf-8")
# print(score_file.read())
# score_file.close()

# score_file:TextIO = open("score.txt","r", encoding="utf-8")
# print(score_file.readline(), end="")
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file= open("score.txt","r",encoding="utf-8")
#
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

score_file= open("score.txt","r",encoding="utf-8")
lines = score_file.readlines()

for line in lines:
    print(line)