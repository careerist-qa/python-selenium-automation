# Created by jacobgrable at 9/22/23
Feature: User verifies something was added to their cart
  # Enter feature description here

  Scenario: User adds something to cart then verifies
  Given Open Amazon Page
    Then Search christmas
  Then Click on Search
  Then Goes to items page
  Then Adds the Item to Cart
  Then Checks their cart
    # Enter steps here