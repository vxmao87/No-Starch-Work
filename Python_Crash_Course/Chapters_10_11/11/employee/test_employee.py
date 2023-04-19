import pytest
from employee import Employee

@pytest.fixture
def current_employee():
    """
    Returns a new Employee as a fixture.
    """
    return Employee("Denny", "Lam", 100000)

def test_give_raise(current_employee):
    current_employee.give_raise()
    assert current_employee.annual_salary == 105000

def test_give_custom_raise(current_employee):
    current_employee.give_raise(100000)
    assert current_employee.annual_salary == 200000