class Student:
    def __init__(self, name, age, college):
        self.name = name
        self.age = age
        self.college = college


a = Student("Mingyo", 20, "Trinity")

print(a.name)
print(a.age)
print(a.college)

class A:
    def intro_a(self):
        print("Hi I am A")

class B:
    def intro_b(self):
        print("Hi I am B")

classroom = [A(),A(),B(),A(),B()]

for person in classroom:
    if isinstance(person, A):
        person.intro_a()
    elif isinstance(person,B):
        person.intro_b()