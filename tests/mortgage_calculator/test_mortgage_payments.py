from decimal import Decimal

import pytest

from mortgage_calculator.mortgage_payments import (
    MortgagePaymentOptions,
    calculate_mortgage_payment,
)


@pytest.mark.parametrize(
    "principal, interest, frequency, years, expected, down_payment",
    [
        (
            Decimal(20_000),
            Decimal(0.0474),
            MortgagePaymentOptions.MONTHLY,
            5,
            Decimal(300),
            Decimal(4_000),
        ),
        (
            Decimal(20_000),
            Decimal(0.0474),
            MortgagePaymentOptions.MONTHLY,
            10,
            Decimal(167),
            Decimal(4_000),
        ),
        (
            Decimal(100_000),
            Decimal(0.05),
            MortgagePaymentOptions.MONTHLY,
            10,
            Decimal(847),
            Decimal(20_000),
        ),
        (
            Decimal(100_000),
            Decimal(0.05),
            MortgagePaymentOptions.ACCELERATED_BIWEEKLY,
            10,
            Decimal(423),
            Decimal(20_000),
        ),
        (
            Decimal(100_000),
            Decimal(0.05),
            MortgagePaymentOptions.BIWEEKLY,
            10,
            Decimal(390),
            Decimal(20_000),
        ),
    ],
)
def test_schedule_payment_amount(principal, interest, frequency, years, expected, down_payment):
    result = calculate_mortgage_payment(
        principal=principal,
        yearly_interest=interest,
        frequency=frequency,
        years=years,
        down_payment=down_payment,
    )

    assert expected == pytest.approx(result, Decimal(0.1))
