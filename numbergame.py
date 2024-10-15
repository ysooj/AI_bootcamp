import random

r_number = random.randint(1, 10)
print("무작위로 1에서 10 사이의 숫자 하나를 골랐습니다. 맞춰보세요")

while True:
    number = int(input("1에서 10 사이의 숫자를 입력하세요: "))

    if number > r_number:
        print("큽니다. 다시 입력해봅시다.: ")

    elif number < r_number:
        print("작습니다. 다시 입력해봅시다.: ")

    else:
        print("정답입니다. 대단해요!")

        break