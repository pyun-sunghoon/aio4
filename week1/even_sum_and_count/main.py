def calculate_even_sum_and_count(n):
    """1부터 n까지의 짝수 합과 개수를 반환한다."""
    total = 0
    count = 0

    if n < 1:
        return {"Sum": 0, "Count": 0}

    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i
            count += 1

    return {"Sum": total, "Count": count}


if __name__ == "__main__":
    n = 10
    print(calculate_even_sum_and_count(n))
