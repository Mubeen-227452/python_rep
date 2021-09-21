class course:
    def __init__(self):
        print("Hi")

    name = "py"
    stud = ["mub", "div", "rah"]


class campus:
    def __init__(self, name):
        self.__name = name
        self.stud = []

    def add_stud(self, student):
        self.stud.append(student)
        self.__write_stud_name(student)

    def stud_count(self):
        return len(self.stud)

    def get_course_name(self):
        return self.__name

    @staticmethod
    def __write_stud_name(student):
        print("hello " + student)


c1 = course()
print(c1.name)
print(c1.stud)

print(type(c1))
c2 = campus("java")
print(c2.stud)
print(c2.get_course_name())
c2.add_stud("rahman")
c2.add_stud("kaja")
print(c2.stud)
print(c2.stud_count())
