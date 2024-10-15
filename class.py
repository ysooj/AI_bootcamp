age = int(input("나이: "))
name = input("이름: ")
gender = input("성별(male 또는 female로 입력해주세요.): ")

class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    def display(self):
        print(f"이름: {self.name}, 성별: {self.gender}")
        print(f"나이: {self.age}")

my_person = Person(name, gender, age)
my_person.display()