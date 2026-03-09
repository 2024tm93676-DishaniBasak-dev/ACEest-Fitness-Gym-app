import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.app import create_app

app = create_app()
client = app.test_client()


def test_home():
    res = client.get("/")
    assert res.status_code == 200


def test_programs():
    res = client.get("/programs")
    assert res.status_code == 200


def test_calorie_calculation():
    res = client.post("/calories", json={
        "weight": 70,
        "program": "Fat Loss"
    })

    assert res.status_code == 200
    assert res.json["calories"] == 1540