# https://www.canada.ca/en/financial-consumer-agency/services/mortgages/down-payment.html

from decimal import Decimal

from mortgage_calculator.constants import (
    FIVE_PERCENT,
    HALF_MILLION,
    ONE_MILLION,
    TEN_PERCENT,
    TWENTY_PERCENT,
)


def validate_low_tier_house_down_payment(down_payment: Decimal, listing_price: Decimal) -> bool:
    return down_payment >= (listing_price * FIVE_PERCENT).quantize(Decimal("0.01"))


def validate_mid_tier_house_down_payment(down_payment: Decimal, listing_price: Decimal) -> bool:
    return down_payment >= ((listing_price - HALF_MILLION) * TEN_PERCENT + FIVE_PERCENT * HALF_MILLION).quantize(
            Decimal("0.01")
        )


def validate_high_tier_house_down_payment(down_payment: Decimal, listing_price: Decimal) -> bool:
    return down_payment >= (TWENTY_PERCENT * listing_price).quantize(Decimal("0.01"))


def validate_minimum_down_payment(listing_price: Decimal, down_payment: Decimal) -> bool:
    if listing_price <= HALF_MILLION:
        return validate_low_tier_house_down_payment(down_payment=down_payment, listing_price=listing_price)
    if HALF_MILLION < listing_price < ONE_MILLION:
        return validate_mid_tier_house_down_payment(down_payment=down_payment, listing_price=listing_price)
    return validate_high_tier_house_down_payment(down_payment=down_payment, listing_price=listing_price)


