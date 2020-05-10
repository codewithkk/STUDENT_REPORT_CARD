class student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.s1 = "WP"
        self.s2 = "PP"
        self.s3 = "IT tools"
        self.s4 = "OOPs"
        self.s5 = "DM"

    def get_subject(self):
        print(self.s1, self.s2, self.s3, self.s4, self.s5)

    def Enter_mark(self):
        print("")
        self.m1 = int(input(self.s1 + ":"))
        self.m2 = int(input(self.s2 + ":"))
        self.m3 = int(input(self.s3 + ":"))
        self.m4 = int(input(self.s4 + ":"))
        self.m5 = int(input(self.s5 + ":"))

    def get_marks(self):
        print(self.s1, " : ", self.m1)
        print(self.s2, " : ", self.m2)
        print(self.s3, " : ", self.m3)
        print(self.s4, " : ", self.m4)
        print(self.s5, " : ", self.m5)

    def Result(self):
        self.res = (self.m1 + self.m2 + self.m3 + self.m4 + self.m5
                    ) / (300) * (100)
        print('\n', 'Result :', self.res)

    def grade(self):
        if self.res >= 80:
            print("A GRADE")
        elif self.res <= 80 and self.res >= 60:
            print("B +  GRADE")
        elif self.res < 60:
            print('B GRADE')
        else:
            print('C GRADE')


n = input('Enter Name: ')
r = input('Enter Roll No. :  ')

s1 = student(n, r)
s1.get_subject()
s1.Enter_mark()
s1.get_marks()
s1.Result()
s1.grade()
