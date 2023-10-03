# Created by jblai at 9/28/2023
Feature: Lesson 7 implement waits

#  Scenario: Verify popup button appears and disappears
#    Given Open Amazon page
#    When Verify Sign-in is clickable
#    When wait for 3 seconds
#    When Verify Sign-in is clickable
#    Then Verify Sign-in disappears
#homework

#  Scenario: Verify cart is empty for a new user
#    Given Open Amazon page
#    When Click Cart
#    Then Verify Your Amazon Cart is empty text is present

  Scenario: Add product to cart and verify product is added
    Given Open Amazon page
    When Search for ball
    Then Verify search result is "ball"
    Then Select Product
    When Store product name
    Then Add product to cart
    Then Verify product is Added to Cart
    Then Verify cart has correct product