# week10_01.py
mydir = "c:\\202444066\\jeondoheon.txt"  # '쓰면 이스케이프가 됨

# 자원 접근 (열기)
# f= open(mydir,'w')  # 쓰기모드
f=open(mydir,'a')  # 추가모드
# 작업
f.write("전도헌\n")


# 자원 해제 (닫기)
f.close()


f1=open(mydir,'r')  # 읽기모드
print(f1.read())    # 작업
f1.close()          # 닫기
