Feature: Shopping Cart

  Scenario: Add product with price greater than $100
    Given an empty cart
    When I add a product with a price of 150
    Then the total should be 135
