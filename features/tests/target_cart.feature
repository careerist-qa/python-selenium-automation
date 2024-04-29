# Created by toshinagpure at 4/8/24
Feature: Target cart tests

  Scenario: “Your cart is empty” message is shown
    Given Open target main page
    When Click on cart icon
    Then Verify 'Your cart is empty' message is shown


  Scenario: Add any product into the cart
    Given Open target main page
    When Search for 'coffee'
    When Click on add to cart button
    When Confirm add to cart button from side navigation
    Then Verify cart has 1 product