# Created by peggyadams at 11/13/23
Feature: Shopping Cart Functionality
  # Enter feature description here

  Scenario: Verify Shopping Cart is Empty
    Given Open target main page
    When Click on Cart Icon
    Then Verify "Your cart is empty"
