# Created by jacobgrable at 9/24/23
Feature: Verify cart is empty
  # Enter feature description here

  Scenario: User checks their cart
    Given Open Amazon page
    When Click on cart icon
    Then Verify 'Your Shopping Cart is empty.' text present