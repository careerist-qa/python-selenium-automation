
Feature: Ensure product is in Cart

  Scenario: User can add cart
    Given Open targets home page
    When Type Banana into search field
    When Click new search button
    When Add to cart
    Then Verify Banana is added in cart
