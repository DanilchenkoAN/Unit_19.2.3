import pytest

from app.calculator import Calculator

class TestCalc:
    def setUp(self):
        self.calc = Calculator

    def test_summ(self):
        assert self.calc.sum(self, 4, 7) == 11

    def test_subtract(self):
        assert self.calc.sub(self, 5, 10) == -5

    def test_multiply(self):
        assert self.calc.mult(self, 3, 7) == 21

    def test_divide(self):
        assert self.calc.div(self, 10, 2) == 5
