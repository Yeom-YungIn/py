#자료 구조의 변경

#커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
menu.append("우유")
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

