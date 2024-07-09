Feature: Target main page Cart functionality tests


  Scenario: Users cart is empty on main page of Target
    Given Open Target main page
    When Clicking on empty cart
    Then  Verify "Your cart is empty" text shown



