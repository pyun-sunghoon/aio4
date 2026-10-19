# What          : 무엇을 만들지
# Consistants   : 어떤 제약으로 동작해야 하는지
# How           : 구현은 어떻게
# Vibe Check    : 결과를 검증

# 3대 핵심 룰 P(Prompt)->G(Genarator)->V(Validator) 사이클
# P(Prompt) : 입력(input), 출력(output), 알고리즘 제약 조건, 함수 명시
# V(Validator) : 결과 검증, 테스트케이스 검증

# 1부터 N까지 짝수 합과 개수 구하기
# Bed : 짝수 합 구해줘
"""
[Problem] 1부터 N까지의 정수 중 짝수들의 합과 짝수의 총 개수를 계산한다.
[Function] calculate_even_sum_and_count(n)
[Rules]
  - n이 1 미만인 경우 합 0, 개수 0을 반환할것
  - for 문과 if 문을 활용하여 짝수(i % 2 == 0)를 판단할 것
[Output] {"Sum":int, "Count":int}
별도의 폴더를 만들고 소스코드를 작성한 후 실행해서 오류가 없는지 확인 할 것
"""

# 실습규칙
'''
문제정의 / 입력값 / 출력값 / 제약조건을 작성
assert 함수를 활용하여 테스트 케이스

[Mission 1: Smart FizzBuzz Analyzer]
- 함수명: analyze_fizzbuzz(limit: int) -> dict
- 로직 제약:
  1. 1부터 limit까지 순회한다.
  2. 3의 배수이면서 5의 배수이면: "FizzBuzz" 카운트 증가
  3. 3의 배수이면: "Fizz" 카운트 증가
  4. 5의 배수이면: "Buzz" 카운트 증가
  5. 그 외의 숫자이면: "Number" 카운트 증가
- 반환값 형식:
  {"FizzBuzz": int, "Fizz": int, "Buzz": int, "Number": int}
- 엣지 케이스: limit가 1 미만인 경우 모든 카운트가 0인 딕셔너리 반환

Mission 1에 해당하는 기능을 정확히 읽고 해당 기능을 다양하게 검증할 수 있도록 assert 키워드를 이용한 검증 파이프라인까지 작성해주세요.
'''
# zip
list_1 = ['a','b','c']
list_2 = [100,200,300]
result = zip(list_1, list_2)

print(result)
for i in result:
     print(type(i))
print(result)
result2 = dict(result)
print(type(result))
print(result2)
print(result)

help(zip)