import pytest

from app.logic import is_eligible_for_loan


def test_eligible_user():
    assert is_eligible_for_loan(60000.0, 22, 'employeed') == True

def test_underage_user():
    assert is_eligible_for_loan(60000.0, 20, 'employeed') == False

def test_low_income():
    assert is_eligible_for_loan(45000, 22, 'employeed') == False

def test_unemployeed():
    assert is_eligible_for_loan(45000, 22, 'unemployeed') == False

def test_boundry():
    assert is_eligible_for_loan(50000, 21, 'employeed') == True