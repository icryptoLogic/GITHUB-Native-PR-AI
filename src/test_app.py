import pytest
from app import add

def test_addition_success():
    assert add(2, 3) == 5

def test_addition_fail():
    # ❌ Intentional failure for demo
    assert add(2, 2) == 5

