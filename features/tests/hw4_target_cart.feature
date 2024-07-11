# Created by jkwak at 7/8/24
Feature: Test Cases for Cart Functionality
  # Test all added products are correctly in the cart.

  Scenario Outline: User can add any 2 products into the cart and make sure it's there
    Given Open target.com
    When Input <product1> in input search
      And Click button search
      And Wait for a banner to unblock
    When Add the first product to cart
      And Click "Add to cart" button
      And Click "Continue shopping" button
      And Clear input search
    When Input <product2> in input search
      And Click button search
    When Add the first product to cart
      And Click "Add to cart" button
      And Click "View cart & check out" button
    Then All the products are shown on the cart
    Examples:
    | product1 | product2 |
    | shoes    | tea      |
    | tea      | shoes    |
