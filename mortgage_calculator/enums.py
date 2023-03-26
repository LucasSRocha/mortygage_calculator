from enum import Enum, IntEnum


class MortgagePaymentOptions(str, Enum):
    BIWEEKLY = "BIWEEKLY"
    ACCELERATED_BIWEEKLY = "ACCELERATED_BIWEEKLY"
    MONTHLY = "MONTHLY"


class MortgagePaymentFrequency(IntEnum):
    BIWEEKLY = 26
    MONTHLY = 12


MORTGAGE_MONTHS_PAYMENTS_MAPPING = {
    MortgagePaymentOptions.BIWEEKLY: (
        12,
        MortgagePaymentFrequency.BIWEEKLY,
    ),
    MortgagePaymentOptions.ACCELERATED_BIWEEKLY: (
        13,
        MortgagePaymentFrequency.BIWEEKLY,
    ),
    MortgagePaymentOptions.MONTHLY: (
        12,
        MortgagePaymentFrequency.MONTHLY,
    ),
}
