import sys
import os
import pytest
from pytest_bdd import scenarios, given, when, then
from app.entities.Cart import Cart  # Ensure the correct import statement

# Add the project root directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Load the scenarios from the feature file
scenarios('test_cart.feature')


@pytest.fixture
def cart():
    return Cart()


@given('an empty cart')
def empty_cart(cart):
    pass


@when('I add a product with a price of 150')
def add_product(cart):
    cart.add_product({'id': 1, 'price': 150})


@then('the total should be 135')
def total_should_be_135(cart):
    assert cart.total() == 135
