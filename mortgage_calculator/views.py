from decimal import Decimal

from fastapi import APIRouter
from pydantic import BaseModel, condecimal, conint, validator

from mortgage_calculator.enums import MortgagePaymentOptions
from mortgage_calculator.mortgage_payments import calculate_mortgage_payment
from mortgage_calculator.validator import validate_minimum_down_payment

router = APIRouter(prefix="/calculator", tags=["calculator"])


class CalculateMortgageSchema(BaseModel):
    listing_price: condecimal(gt=0)
    yearly_interest: condecimal(gt=0, le=1)
    years: conint(ge=5, le=30)
    frequency: MortgagePaymentOptions = MortgagePaymentOptions.MONTHLY
    down_payment: condecimal(ge=0)

    @validator("down_payment")
    def validate_down_payment_amount(cls, v, values):
        value = Decimal(v)
        listing_price = values.get("listing_price", 0)
        if not validate_minimum_down_payment(listing_price=listing_price, down_payment=value):
            raise ValueError("Down Payment insuficient for the Listing Price")
        elif value > listing_price:
            raise ValueError("Down Payment is bigger than the Listing Price")
        elif value == listing_price:
            raise ValueError("Down Payment is equal to the Listing Price")

        return value


@router.post("/")
def calculate_mortgage_payments(body: CalculateMortgageSchema):
    return {
        "payment_amount": calculate_mortgage_payment(
            listing_price=body.listing_price,
            yearly_interest=body.yearly_interest,
            years=body.years,
            frequency=body.frequency,
            down_payment=body.down_payment,
        )
    }
