import random


def practice_5():
    """실습 5: 숫자 맞추기 게임 (원본: day1-5.py)

    핵심: random.randint(1, 100)은 1과 100을 포함해 정수를 고릅니다.
          while은 조건이 참인 동안 반복합니다.
          !=는 서로 다른지, ==는 서로 같은지 비교합니다.
    실행 방법: 숫자를 입력하고 '큽니다/작습니다' 힌트로 정답을 찾습니다.
    추가 연습:
        - 정답 범위를 1~50으로 바꾸어 보세요.
        - 시도 횟수를 변수에 저장하고 정답을 맞히면 출력해 보세요.
        - while True와 break를 사용해 같은 게임을 만들어 보세요.
    """
    com_number = random.randint(1, 100)
    user_number = 0

    while com_number != user_number:
        user_number = int(input("1~100 : "))
        if user_number > com_number:
            print("컴퓨터보다 큽니다.")
        elif user_number < com_number:
            print("컴퓨터보다 작습니다.")
        else:
            print("정답입니다.")
