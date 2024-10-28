class student:
    grade = 10
    name = "Penguin"

    def intoduction(self):
        print("I am a student")

    def details(self):
            print("My name is", self.name)
            print("I study in Grade", self.grade)

ob = student()
ob.intoduction()
ob.details()