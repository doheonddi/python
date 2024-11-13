# week12_10.py

file = "c:/abc/abc.txt"

f = None
try:
    f = open(file, "r")
except:  # 모든 Error 처리
    print(file, "이 없어요.")
finally:
    if f != None:
        f.close()

def test():
    raise NotImplementedError("구현해")

        
while True:    
    try:
        dvd = int(input("분자: "))
        dvs = int(input("분모: "))
        result = dvd / dvs
        print(result)
        test()
    except ValueError:  # value 에러만 처리
        print("정수만 넣으세요")
    except ZeroDivisionError as ze:
        print(ze)
        print("분모는 0 넣으면 안됩니다.")
    except Exception as e:
        print(e)
    else:
        # try 구문이 정상적으로 실행되면 실행
        print("성공!")
    finally:
        print("안녕히 계세요 여러분~!")

'''
    except Exception:
        print("잘못되었습니다")
    except:
        print("정수만 넣으세요")
'''
