Feature: Cart tests

  Scenario: 'Your cart is empty' message is shown
    Given Open Target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown