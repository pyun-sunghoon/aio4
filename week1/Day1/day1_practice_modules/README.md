# Python 기초 복습 실습

다섯 실습을 별도 모듈로 분리했습니다. Python 3만 있으면 실행할 수 있으며 외부 패키지는 필요하지 않습니다.

## 실행

PowerShell에서 새 폴더로 이동한 후 실행합니다.

```powershell
cd C:\AIO4\day1_practice_modules
python main.py
```

상위 폴더에서 패키지로 실행할 수도 있습니다.

```powershell
cd C:\AIO4
python -m day1_practice_modules
```

기존 명령인 `python day1_practice.py`도 같은 메뉴를 실행합니다. 환경에 따라 `python` 대신 `py` 또는 `python3`를 사용하세요.

## 파일 구성

```text
day1_practice_modules/
├── __init__.py              # 패키지 표시
├── __main__.py              # python -m 실행 진입점
├── main.py                  # 메뉴, 실습 호출, 입력 오류·종료 처리
├── README.md                # 실행 및 실습 안내
└── exercises/
    ├── __init__.py          # 실습 패키지 표시
    ├── variables.py         # 1. 변수와 산술 연산
    ├── conditions.py        # 2. 입력과 합격 판정
    ├── lists.py             # 3. 리스트와 짝수 판별
    ├── multiplication.py    # 4. 중첩 반복문과 구구단
    └── guessing_game.py     # 5. random과 숫자 맞추기
```

## 실습 방법

1. `exercises` 폴더에서 원하는 파일을 엽니다.
2. 함수 안의 설명, 예상 결과, 추가 연습 과제를 읽습니다.
3. 메뉴를 실행하고 해당 번호를 선택합니다. `0`은 종료입니다.
4. 해당 실습 함수를 수정하고 프로그램을 다시 실행합니다.

입력 실습에서는 정수를 입력하세요. 정수가 아닌 값은 안내 후 메뉴로 돌아갑니다. 숫자 맞추기는 정답을 맞힐 때까지 진행되며 `Ctrl+C`로 프로그램을 종료할 수 있습니다.

`main.py`는 각 모듈의 함수를 `import`하여 호출합니다. 실습 모듈을 가져오는 것만으로는 메뉴나 게임이 시작되지 않습니다. 함수는 여러 동작을 이름으로 묶고, 모듈은 관련 코드를 별도 파일로 나누는 역할을 합니다.
