# week12_01.py

class Subject:  # Subjecct() -> __new()__ -> __init()__
    def __init__(self, number, name, teacher=None, grade=None):  # None은 일종의 null
        self.number = number
        self.name = name
        self.teacher = teacher
        self.setGrade(grade)

    def __str__(self):
        return f"[{self.number}] {self.name}"

    def setGrade(self, grade):
        if grade != None:
            if grade < 0:
                grade = 0.0
            elif grade > 4.5:
                grade = 4.5
        self.grade = grade

# sub1 = Subject("0001", "컴퓨터공학분석", grade=1000.9)
# print(sub1.grade)
# sub1.grade = 1000.9
# print(sub1.grade)
# sub1.setGrade(1000.9)
# print(sub1.grade)


class Student:
    def __init__(self, number, name, dept, birthyear, *subjects):  # *subjects는 튜플
        self.number = number
        self.name = name
        self.dept = dept
        self.birthyear = birthyear
        if subjects:
            self.subjects = list(subjects)
        else:
            self.subjects = list()
        
    def __str__(self):
        return f"[{self.number}] {self.name}"

    def total_grade(self):
        if self.subjects:
            grades = [subject.grade for subject in self.subjects if subject.grade != None]
        if grades:
            return sum(grades) / len(grades)
        else:
            # print("수강과목이 없음")
            return None


sub1 = Student("1", "전도헌", "컴정", "2005", 2024)
print(sub1)
print(sub1.total_grade())

sub2 = Student("1", "전도헌", "컴정", "2005", 2024, Subject("1", "파이썬", "장은미"),
                                                    Subject("2", "자바스크립트", "전혜경"))
print(sub2)
print(sub2.total_grade())

sub3= Student("1", "전도헌", "컴정", "2005", 2024, Subject("1", "파이썬", "장은미"),
                                                    Subject("2", "자바스크립트", "전혜경"),
                                                    Subject("3", "오픈소스", "김태간"))
print(sub3)
print(sub3.total_grade())
