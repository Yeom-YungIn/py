#빈 자리는 빈공간으로 두고, 오른쪽 정렬, 총 10자리 확보
print("{0: >10}".format(500))

#양수일때는 + 음수일때는 -
print("{0: >+5}".format(500))
print("{0: >+10}".format(-500))

#왼쪽정렬, 빈칸 _
print("{0:_<+10}".format(500))

#3자리마다 콤마
print("{0:,}".format(10000000))
#부호도 같이
print("{0:+,}".format(10000000))
print("{0:+,}".format(-10000000))

#3자리마다 콤마, 자리수 확보
print("{0:_>+10,}".format(10000))

#소수점 출력
print("{0:f}".format(5/3))
#두번쨰자리 까지만
print("{0:.2f}".format(5/3))

