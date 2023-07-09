# Created by domon at 5/7/2023
Feature: User Should See New Item in Cart after Adding


  Scenario: Add Item to Cart
    Given Go to keyboard item page
    When Click add to cart button
    Then Verify added to cart