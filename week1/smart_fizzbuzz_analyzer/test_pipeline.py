"""실행: python smart_fizzbuzz_analyzer/test_pipeline.py"""

from main import analyze_fizzbuzz


def run_validation_pipeline() -> None:
    """하나라도 조건을 만족하지 않으면 AssertionError로 검증을 중단한다."""
    if not __debug__:
        raise RuntimeError("assert 검증을 위해 -O 또는 -OO 옵션 없이 실행하세요.")

    # 1. 빈 범위, 각 분류의 첫 등장, 공배수 전후, 대표 입력 검증
    cases = [
        (-100, {"FizzBuzz": 0, "Fizz": 0, "Buzz": 0, "Number": 0}),
        (-1, {"FizzBuzz": 0, "Fizz": 0, "Buzz": 0, "Number": 0}),
        (0, {"FizzBuzz": 0, "Fizz": 0, "Buzz": 0, "Number": 0}),
        (1, {"FizzBuzz": 0, "Fizz": 0, "Buzz": 0, "Number": 1}),
        (2, {"FizzBuzz": 0, "Fizz": 0, "Buzz": 0, "Number": 2}),
        (3, {"FizzBuzz": 0, "Fizz": 1, "Buzz": 0, "Number": 2}),
        (5, {"FizzBuzz": 0, "Fizz": 1, "Buzz": 1, "Number": 3}),
        (14, {"FizzBuzz": 0, "Fizz": 4, "Buzz": 2, "Number": 8}),
        (15, {"FizzBuzz": 1, "Fizz": 4, "Buzz": 2, "Number": 8}),
        (16, {"FizzBuzz": 1, "Fizz": 4, "Buzz": 2, "Number": 9}),
        (29, {"FizzBuzz": 1, "Fizz": 8, "Buzz": 4, "Number": 16}),
        (30, {"FizzBuzz": 2, "Fizz": 8, "Buzz": 4, "Number": 16}),
        (31, {"FizzBuzz": 2, "Fizz": 8, "Buzz": 4, "Number": 17}),
        (100, {"FizzBuzz": 6, "Fizz": 27, "Buzz": 14, "Number": 53}),
        (100_000, {"FizzBuzz": 6666, "Fizz": 26667, "Buzz": 13334, "Number": 53333}),
    ]
    for limit, expected in cases:
        actual = analyze_fizzbuzz(limit)
        assert actual == expected, f"limit={limit}: expected={expected}, actual={actual}"

    # 2. 반복문과 독립적인 배수 개수 수식으로 연속 입력을 교차 검증한다.
    for limit in range(-10, 1001):
        n = max(limit, 0)
        common = n // 15
        expected = {
            "FizzBuzz": common,
            "Fizz": n // 3 - common,
            "Buzz": n // 5 - common,
            "Number": n - n // 3 - n // 5 + common,
        }
        actual = analyze_fizzbuzz(limit)
        assert type(actual) is dict, f"limit={limit}: 반환값은 dict여야 합니다."
        assert set(actual) == set(expected), f"limit={limit}: 키가 다릅니다."
        assert all(type(v) is int and v >= 0 for v in actual.values()), (
            f"limit={limit}: 카운트는 0 이상의 정수여야 합니다."
        )
        assert sum(actual.values()) == n, f"limit={limit}: 총합이 다릅니다."
        assert actual == expected, f"limit={limit}: expected={expected}, actual={actual}"

    # 3. 결과를 수정해도 다른 호출의 결과에 영향을 주지 않아야 한다.
    for limit in (0, 15):
        first = analyze_fizzbuzz(limit)
        second = analyze_fizzbuzz(limit)
        assert first is not second, "호출마다 새 딕셔너리를 반환해야 합니다."
        first["FizzBuzz"] = -1
        assert second["FizzBuzz"] >= 0, "호출 사이에 결과가 공유됩니다."
        assert analyze_fizzbuzz(limit) == second, "이전 결과 수정이 다음 호출에 영향을 줍니다."

    print(f"검증 성공: 대표값 {len(cases)}개, 연속 입력 1,011개, 결과 독립성 2개")


if __name__ == "__main__":
    run_validation_pipeline()
