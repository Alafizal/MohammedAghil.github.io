class Student:
    def __init__(self, name, age, phone_no, weight, height): 
        self.nm = name
        self.ag = age
        self.pn = phone_no
        self.hi = height
        self.wg = weight

    def adult(self):
        if self.ag >= 18:
            return "adult"
        else:
            return "minor"

    def bmi(self):
        return (self.wg/(self.hi*self.hi))

    def display(self):
        print("Printing details of student whose name is", self.nm)
        print("The phone number of the student is", self.pn)
        print("The weight and height of", self.nm, "is", self.wg, "and", self.hi)
        print("The age of ", self.nm, "is", self.ag)
        print("This student is now considered as an", self.adult())
        print("BMI of this student is", self.bmi())

s1 = Student("Ala", 18, 7012492193, 50, 5)
s1.display()