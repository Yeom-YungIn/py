def profile(name, age, main_lang):
    print(name, age, main_lang)

# 파라미터 순서대로 넣지 않아도 호출 가능
profile(age= 20, name="김땜떙", main_lang="JAVA")

#가변인자
#파라미터가 여러개로 늘어날경우
def profile(name, age, lang1, lang2, lang3):
    print(name, age, lang1, lang2, lang3)

# 아래와 같이 가변인자를 추가
def profile(name, age, *language):
    print(name, age, *language)

#아래와같이 여러파라미터를 넣어도 실행가능
profile("김떙떙", 29, "JAVA", "JS", "PYTHON", "JAVA", "JS", "PYTHON", "JAVA", "JS", "PYTHON")