# Created by jblai at 9/20/2023
Feature: Open Best Sellers page and verify that it is correct

  Scenario: Open the Best Sellers page
    Given Open Amazon page
    When Open Hamburger Menu
    Then Open Best Sellers Page
    Then Verify Bestsellers page is opened


  Scenario: Add product to cart and verify product is added
    Given Open Amazon page
    When Search for <ball>
    Then Verify search result is <ball>
    Then Select Product
    Then Add product to cart
    Then Verify product is added to cart