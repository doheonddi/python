#week03_07.py
test="i am a BOY."

print(test.count("a"))
print(test.count("A"))

print(test.find("a"))
print(test.find("q")) #find는 오류 발생 시 -1 반환
print(test.count("m"))
print(test.count("q"))

print(test.index("a"))
#print(test.index("A")) #index는 오류 발생 죽음 
print(test.index("am"))
if "qm" in test:
    print(test.index("qm"))

print(test.upper()) #대문자
print(test.lower()) #소문자
print(test.title()) #단어마다 첫 글자 대문자
print(test.capitalize()) #문장 첫 글자 대문자
print("/".join(test)) #/ 삽입(공백 포함)

test="  JMT University   "
print(test)
print("|"+test.strip()+"|") #공백 지움
print("|"+test.lstrip()+"|") #왼쪽 공백 지움
print("|"+test.rstrip()+"|") #오른쪽 공백 지
print(test)

print(test.replace("University", "High School"))
# University 를 High School로 바꿈(기존 test가 바뀐 건 아님!)

print(test.split()) #공백, \n 나누기
print(test.split("i")) #기준 i를 잡아서 나누기(i는 사라짐)

'''a="%d%%"%10
print(a)
10%가 출력 됨. 포매팅 연산자 %d와 %를 같이 쓸 떄는 %%를 쓴다.
'''
