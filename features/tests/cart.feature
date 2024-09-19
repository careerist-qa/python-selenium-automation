# Created by LOPA at 9/17/2024
Feature: Test for cart functionality

  Scenario: User can see Cart Empty message
    Given Open target main page
    When Click on cart icon
    Then Verify cart Empty message shown


Scenario: User can add a product to cart
    Given Open target main page
    When Search for tea
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product