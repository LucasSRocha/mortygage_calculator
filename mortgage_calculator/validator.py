# https://www.canada.ca/en/financial-consumer-agency/services/mortgages/down-payment.html

from decimal import Decimal

from mortgage_calculator.constants import (
    FIVE_PERCENT,
    HALF_MILLION,
    ONE_MILLION,
    TEN_PERCENT,
    TWENTY_PERCENT,
)


def validate_low_tier_house_down_payment(down_payment: Decimal, principal: Decimal) -> bool:
    return down_payment >= (principal * FIVE_PERCENT).quantize(Decimal("0.01"))


def validate_mid_tier_house_down_payment(down_payment: Decimal, principal: Decimal) -> bool:
    return down_payment >= ((principal - HALF_MILLION) * TEN_PERCENT + FIVE_PERCENT * HALF_MILLION).quantize(
            Decimal("0.01")
        )


def validate_high_tier_house_down_payment(down_payment: Decimal, principal: Decimal) -> bool:
    return down_payment >= (TWENTY_PERCENT * principal).quantize(Decimal("0.01"))


def validate_minimum_down_payment(principal: Decimal, down_payment: Decimal) -> bool:
    if principal <= HALF_MILLION:
        return validate_low_tier_house_down_payment(down_payment=down_payment, principal=principal)
    if HALF_MILLION < principal < ONE_MILLION:
        return validate_mid_tier_house_down_payment(down_payment=down_payment, principal=principal)
    return validate_high_tier_house_down_payment(down_payment=down_payment, principal=principal)


