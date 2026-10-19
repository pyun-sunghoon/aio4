def practice_3():
    """실습 3: 리스트와 반복문, 짝수 판별 (원본: day1-3.py)

    핵심: []로 리스트를 만들고 append()로 값을 추가합니다.
          range(5)는 0부터 4까지, 총 다섯 번 반복합니다.
          숫자 % 2가 0이면 짝수입니다.
          f-string은 문자열 안에 변수나 계산 결과를 넣습니다.
    확인 입력: 1, 2, 3, 4, 5 → 리스트 출력 후 2와 4 출력
    추가 연습:
        - 홀수만 출력하도록 조건을 바꾸어 보세요.
        - 입력받는 개수를 5개에서 10개로 바꾸어 보세요.
        - sum(scores)로 입력한 숫자의 합을 출력해 보세요.
    """
    scores = []
    for i in range(5):
        scores.append(int(input(f"{i + 1} : 숫자를 입력하세요 : ")))

    print("리스트변수의 값 : ", scores)
    for number in scores:
        if number % 2 == 0:
            print(number)
