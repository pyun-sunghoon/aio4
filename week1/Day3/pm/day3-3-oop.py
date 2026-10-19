"""주문 정보와 계산 동작을 Order 객체로 묶은 객체지향 예제입니다."""

from dataclasses import dataclass
from typing import ClassVar


# 리팩토링: 함수의 인수를 객체의 속성으로, 계산 동작을 메서드로 옮깁니다.
# frozen=True로 생성 후 속성 변경을 막아 검증된 주문 정보를 유지합니다.
@dataclass(frozen=True)
class Order:
    """검증된 주문 정보입니다. 가격은 원 단위 정수, 수량은 양의 정수입니다.

    회원 유형은 0(일반), 1(5%), 2(10%), 3(20%)입니다.
    쿠폰은 YES/NO 문자열이며 대소문자와 앞뒤 공백은 무시합니다.
    """

    u_type: int
    price: int
    qty: int
    coupon: str

    # 리팩토링: 모든 주문에 공통인 할인 정책을 클래스 변수로 관리합니다.
    DISCOUNT_PERCENT_BY_TYPE: ClassVar[dict[int, int]] = {
        0: 0,
        1: 5,
        2: 10,
        3: 20,
    }
    COUPON_AMOUNT: ClassVar[int] = 3000

    def __post_init__(self) -> None:
        # 리팩토링: dataclass의 생성자 실행 직후 입력을 검증합니다.
        # 잘못된 주문은 객체 생성 단계에서 예외가 발생합니다.
        self._validate()

        # 불변 객체의 초기화 과정에서만 정규화된 쿠폰 값을 저장합니다.
        object.__setattr__(self, "coupon", self.coupon.strip().upper())

    def _validate(self) -> None:
        """입력 타입과 범위를 검증합니다. bool은 정수 입력으로 허용하지 않습니다."""
        for name, value in (
            ("u_type", self.u_type),
            ("price", self.price),
            ("qty", self.qty),
        ):
            if type(value) is not int:
                raise TypeError(f"{name}은 bool이 아닌 정수여야 합니다.")

        if self.u_type not in self.DISCOUNT_PERCENT_BY_TYPE:
            raise ValueError("u_type은 0, 1, 2, 3 중 하나여야 합니다.")
        if self.price < 0:
            raise ValueError("price는 0 이상이어야 합니다.")
        if self.qty < 1:
            raise ValueError("qty는 1 이상이어야 합니다.")
        if not isinstance(self.coupon, str):
            raise TypeError("coupon은 YES 또는 NO 문자열이어야 합니다.")
        if self.coupon.strip().upper() not in ("YES", "NO"):
            raise ValueError("coupon은 YES 또는 NO여야 합니다.")

    def calculate_total(self) -> int:
        """회원 할인 → 쿠폰 차감 → 최저 0원 제한 → 원 미만 절삭 순으로 계산합니다."""
        # 리팩토링: 인수를 다시 전달하지 않고 객체에 저장된 주문 정보를 사용합니다.
        remaining_percent = 100 - self.DISCOUNT_PERCENT_BY_TYPE[self.u_type]

        # 기존 개선 유지: 정수로 금액의 100배를 계산해 float 오차를 방지합니다.
        total_scaled = self.price * self.qty * remaining_percent
        if self.coupon == "YES":
            total_scaled -= self.COUPON_AMOUNT * 100

        return max(0, total_scaled) // 100


if __name__ == "__main__":
    # 사용법 변경: 주문 객체를 생성한 후 계산 메서드를 호출합니다.
    order = Order(u_type=1, price=100, qty=20, coupon="YES")
    print(order.calculate_total())
