import pytest
from app.utils.validator import Validator

def test_validate():
    assert Validator.validate(True) == True

def test_validate():
    assert Validator.validate(False) == False