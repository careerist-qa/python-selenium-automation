# Created by jkwak at 7/22/24

Feature: Test Scenario for Cart Functionality by Page Objects
  # Verify "Your cart is empty" message when the cart is empty.

  Scenario: Hw6 Your cart is empty
    Given Open target main page by Page
    When Click on Cart icon by Page
    Then Verify "Your cart is empty" message is shown by Page