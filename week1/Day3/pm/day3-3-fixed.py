"""주문 금액 계산 개선 예제: 금액은 원 단위 정수로 받습니다."""


# 수정: 회원 유형과 할인율의 의미를 상수로 명시합니다.
# 정책: 0은 일반 회원, 1/2/3은 각각 5%/10%/20% 할인 회원입니다.
DISCOUNT_PERCENT_BY_TYPE = {0: 0, 1: 5, 2: 10, 3: 20}
COUPON_AMOUNT = 3000


def calc_order_legacy(u_type: int, price: int, qty: int, coupon: str) -> int:
    """회원 할인 후 쿠폰을 적용하고, 최저 0원으로 제한한 뒤 원 미만을 버립니다.

    price는 0 이상의 원 단위 정수, qty는 1 이상의 정수여야 합니다.
    coupon은 YES 또는 NO이며 대소문자와 앞뒤 공백은 무시합니다.
    타입이 맞지 않으면 TypeError, 허용 범위를 벗어나면 ValueError를 냅니다.
    """
    # 수정: bool도 int의 하위 타입이므로 정확한 int인지 검사합니다.
    # 잘못된 가격/수량을 마지막의 0원 제한 처리로 숨기지 않습니다.
    for name, value in (("u_type", u_type), ("price", price), ("qty", qty)):
        if type(value) is not int:
            raise TypeError(f"{name}은 bool이 아닌 정수여야 합니다.")

    if u_type not in DISCOUNT_PERCENT_BY_TYPE:
        raise ValueError("u_type은 0, 1, 2, 3 중 하나여야 합니다.")
    if price < 0:
        raise ValueError("price는 0 이상이어야 합니다.")
    if qty < 1:
        raise ValueError("qty는 1 이상이어야 합니다.")

    # 수정: 문자열을 정규화하고, 잘못된 쿠폰 값은 명확히 거부합니다.
    if not isinstance(coupon, str):
        raise TypeError("coupon은 YES 또는 NO 문자열이어야 합니다.")
    normalized_coupon = coupon.strip().upper()
    if normalized_coupon not in ("YES", "NO"):
        raise ValueError("coupon은 YES 또는 NO여야 합니다.")

    # 수정: float 대신 정수 백분율을 사용해 큰 금액의 정밀도를 보장합니다.
    # 계산 중에는 금액의 100배를 유지해 마지막까지 소수 부분을 보존합니다.
    remaining_percent = 100 - DISCOUNT_PERCENT_BY_TYPE[u_type]
    total_scaled = price * qty * remaining_percent

    # 기존 정책 유지: 회원 할인 다음에 쿠폰을 차감합니다.
    if normalized_coupon == "YES":
        total_scaled -= COUPON_AMOUNT * 100

    # 수정: 최저 0원 제한 후 정수 나눗셈으로 최종 원 미만 절삭을 명시합니다.
    return max(0, total_scaled) // 100


# 수정: import할 때 예제가 자동 실행되지 않도록 보호합니다.
if __name__ == "__main__":
    result = calc_order_legacy(1, 100, 20, "YES")
    print(result)
