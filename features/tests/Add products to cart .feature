
Feature: Adding a product to cart

  Scenario: User will be able to add a product into their cart
    Given Open Target page
    When Click on Categories
    When Click on Grocery
    When Click on Snacks
    When Click on Chips
    When Click on Add to cart for Doritos
    When Click on Add to cart side nav
    When Click on view cart and checkout button
    Then Verify if {product} is shown
