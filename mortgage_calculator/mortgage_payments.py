from decimal import Decimal

from .enums import MORTGAGE_MONTHS_PAYMENTS_MAPPING, MortgagePaymentOptions


def monthly_mortgage_payment(
    principal: Decimal,
    yearly_interest: Decimal,
    years: int,
) -> Decimal:
    n_lifetime_payments = years * 12
    monthly_interest = yearly_interest / 12
    mortgage_interest = (1 + monthly_interest) ** n_lifetime_payments
    return principal * (monthly_interest * mortgage_interest) / (mortgage_interest - 1)


def calculate_mortgage_payment(
    principal: Decimal,
    yearly_interest: Decimal,
    years: int,
    frequency: MortgagePaymentOptions,
    down_payment: Decimal,
) -> Decimal:
    adjusted_principal = principal - down_payment
    adjusted_months, adjusted_frequency = MORTGAGE_MONTHS_PAYMENTS_MAPPING[frequency]
    monthly_payment = monthly_mortgage_payment(
        principal=adjusted_principal, yearly_interest=yearly_interest, years=years
    )
    adjusted_payment = monthly_payment * adjusted_months / adjusted_frequency
    return adjusted_payment.quantize(Decimal("0.01"))
