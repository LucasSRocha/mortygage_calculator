import pytest

from mortgage_calculator.validator import Decimal, validate_minimum_down_payment


@pytest.mark.parametrize(
    "principal, down_payment, expected",
    [
        (Decimal(10_000), Decimal(500), True),
        (Decimal(10_000), Decimal(400), False),
        (Decimal(500_000), Decimal(25_000), True),
        (Decimal(500_000), Decimal(27_000), True),
        (Decimal(500_001), Decimal(25_000), False),
        (Decimal(500_001), Decimal("25_000.10"), True),
        (Decimal(600_000), Decimal(35_000), True),
        (Decimal(600_000), Decimal(50_000), True),
        (Decimal(1_000_000), Decimal(199_999), False),
        (Decimal(1_000_000), Decimal(200_000), True),
        (Decimal(1_000_000), Decimal(999_999), True),
    ],
)
def test_minimum_down_payment(principal, down_payment, expected):
    assert validate_minimum_down_payment(principal=principal, down_payment=down_payment) == expected
