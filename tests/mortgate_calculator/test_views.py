import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


@pytest.fixture
def mortgage_view_payload():
    return {
        "principal": 10_000,
        "yearly_interest": 0.05,
        "years": 5,
        "frequency": "MONTHLY",
        "down_payment": 5_000,
    }


def test_calculate_mortgage_payments_view_200(mortgage_view_payload):
    resp = client.post("/calculator", json=mortgage_view_payload)
    assert resp.status_code == 200
    assert resp.json() == {"payment_amount": 94.36}


@pytest.mark.parametrize(
    "payload",
    [
        {"principal": 5_000, "down_payment": 10_000},
        {"principal": 5_000, "down_payment": 5_000},
        {"principal": 100_000, "down_payment": 1_000},
        {"years": 4},
        {"years": 31},
        {"yearly_interest": 0},
        {"yearly_interest": 1.2},
        {"frequency": "SOME_STRING"},
    ],
)
def test_calculate_mortgage_payments_view_validation_errors(payload, mortgage_view_payload):
    mortgage_view_payload.update(payload)
    resp = client.post("/calculator", json=mortgage_view_payload)
    assert resp.status_code == 422
