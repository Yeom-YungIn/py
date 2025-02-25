weather = input("오늘 날씨는 어때요?")

if weather == "비" or weather == "눈":
    print("우산을 챙겨라")
elif weather == "미세먼지":
    print("마스크를 챙겨라.")
else:
    print("출근이나 해라")


temp = int(input("오늘 몇도야"))

if 30 < temp:
    print("끔찍")
elif temp < 30  and temp > 10:
    print("덜 끔찍")
elif (temp < -10) and (temp > -100):
    print("꽁꽁")
