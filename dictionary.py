# Dictionary

cabinet = { 3: "김아무개", 100: "박아무개"}
print(cabinet)
print(cabinet[3])
print(cabinet[100])
# print(cabinet[101]) err

print(cabinet.get(3))
print(cabinet.get(5)) #None
print(cabinet.get(5, "비어 있음")) #비어 있음

print(3 in cabinet) #True
print(5 in cabinet) #False

cabinet = { "a1": "김아무개", "a2": "박아무개"}

print(cabinet["a1"])

cabinet["a3"] = "최아무개"
print(cabinet)
print(cabinet["a3"])
cabinet["a3"] = "이아무개"
print(cabinet["a3"])
print(cabinet.get("A3"))

print(cabinet.keys())
print(cabinet.keys().mapping)
print(len(cabinet.keys()))

cabinet2 = cabinet.copy()
print(cabinet2)
print(cabinet.values())
print(cabinet.items())

del cabinet["a3"]
print(cabinet.get("a3"))

cabinet.clear()
print(cabinet)

