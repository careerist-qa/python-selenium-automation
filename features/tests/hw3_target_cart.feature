# Created by jkwak at 7/2/24
Feature: Test Scenario for Cart Functionality
  # Verify an empty cart when the cart has 0 item.

  Scenario: User can check an empty cart
    Given Open target.com
    When Click on Cart icon
    Then Verify "Your cart is empty" message is shown
