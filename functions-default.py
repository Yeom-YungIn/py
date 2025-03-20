def profile(name, age, main_lang):
    print("이름 : {0}\t 나이 : {1} \t 주 사용 언어 : {2}".format(name, age, main_lang))

profile("김땡떙", 20 , "JAVA")

def profile(name, age=17, main_lang="PYTHON"):
    print("이름 : {0}\t 나이 : {1} \t 주 사용 언어 : {2}".format(name, age, main_lang))

profile("김땡떙")
profile("이땡떙", 20 , "JAVA")
