import random   # random 모듈 불러오기

r_number = random.randint(1, 10)    # random 모듈의 randint 함수
print("무작위로 1에서 10 사이의 숫자 하나를 골랐습니다. 맞춰보세요")

while True: # while문을 사용해서 참인 동안 반복하기
    number = int(input("1에서 10 사이의 숫자를 입력하세요: "))  # 사용자의 입력을 받을 부분

    if number > r_number:   # 사용자가 입력한 숫자가 컴퓨터가 정한 숫자보다 큰 경우
        print("큽니다. 다시 입력해봅시다.: ")

    elif number < r_number: # 사용자가 입력한 숫자가 컴퓨터가 정한 숫자보다 작은 경우
        print("작습니다. 다시 입력해봅시다.: ")

    else:   # 정답인 경우
        print("정답입니다. 대단해요!")

        break   # break로 while을 종료시킨다.