"""실습 메뉴와 실행 진입점. 직접 실행하거나 python -m으로 실행하세요."""

if __package__:
    from .exercises.variables import practice_1
    from .exercises.conditions import practice_2
    from .exercises.lists import practice_3
    from .exercises.multiplication import practice_4
    from .exercises.guessing_game import practice_5
else:
    from exercises.variables import practice_1
    from exercises.conditions import practice_2
    from exercises.lists import practice_3
    from exercises.multiplication import practice_4
    from exercises.guessing_game import practice_5


def main():
    # 함수는 실행할 코드를 이름으로 묶습니다. 아래에서 선택한 함수를 호출합니다.
    practices = {
        "1": practice_1,
        "2": practice_2,
        "3": practice_3,
        "4": practice_4,
        "5": practice_5,
    }

    while True:
        print("\n=== Python 기초 복습 실습 ===")
        print("1. 변수와 산술 연산")
        print("2. 점수 입력과 합격 판정")
        print("3. 리스트에 숫자를 저장하고 짝수 출력")
        print("4. 중첩 반복문으로 구구단 출력")
        print("5. 숫자 맞추기 게임")
        print("0. 종료")
        choice = input("실습 번호를 선택하세요 : ").strip()

        if choice == "0":
            print("실습을 종료합니다.")
            break
        if choice not in practices:
            print("0~5 중에서 선택하세요.")
            continue

        practice = practices[choice]
        print(f"\n{practice.__doc__}")
        try:
            practice()
        except ValueError:
            print("정수를 입력해야 합니다. 메뉴에서 실습을 다시 선택하세요.")


def run():
    """사용자 종료 요청을 처리하며 메뉴를 실행합니다."""
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n실습을 종료합니다.")


if __name__ == "__main__":
    run()
