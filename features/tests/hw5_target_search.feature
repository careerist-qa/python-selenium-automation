# Created by jkwak at 7/15/24
Feature: Test Cases for ADD Functionality
  # Enter feature description here

  Scenario Outline: User can add a product to cart
    Given Open target main page
    When Search for <product>
      And Click on Add to Cart button
      And Store product name
      And Confirm Add to Cart button from side navigation
      And Open cart page
    Then Verify cart has <amount> itme(s)
      And Verify cart has correct product
    Examples:
    | product | amount |
    | mug     | 1      |
    | mug     | 1      |
    | mug     | 1      |