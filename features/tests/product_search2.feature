# Created by willi at 5/14/2026

Feature: Target Empty Cart
  # Your cart is empty

  ##Homework 6
  Scenario: Verify cart page is empty
    Given Open target.com
    When I click on the cart icon
    Then I should see "Your cart is empty"