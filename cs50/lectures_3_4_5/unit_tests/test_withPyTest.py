# ==========================
# Unit testing with "pytest" and assert
# ===========================
from calculator import square

# Test 1
def test_positive():
    assert square(2) == 4
    assert square(3) == 9

# Test 2
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

# Test 3
def test_zero():
    assert square(0) == 0

