# 사용자에게 입력받을 곳
age = int(input("나이: "))
name = input("이름: ")
gender = input("성별(male 또는 female로 입력해주세요.): ")

class Person:   # Person이라는 class
    def __init__(self, name, gender, age):  # 생성자 __init__을 통해 객체 생성 시 이름, 성별, 나이를 초기화
        self.name = name    # 매개 변수 name
        self.gender = gender    # 매개 변수 gender
        self.age = age  # 매개 변수 age
    def display(self):  # 정보를 출력하는 함수
        print(f"이름: {self.name}, 성별: {self.gender}")    # 이름과 성별은 같은 행에 출력.
        print(f"나이: {self.age}")  # 나이는 다음 행에 출력
        # f스트링으로 문자열 안에 변수를 받는다.

my_person = Person(name, gender, age)   # Person 객체를 생성한다.
my_person.display() # display()함수를 통해 객체의 정보를 출력한다.