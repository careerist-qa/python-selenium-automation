# Created by domon at 5/25/2023
Feature: Product option verification
  # Enter feature description here

  Scenario: Go to product page and check color options
    Given Open jeans product page
    When Verify there are 19 color options
    Then Verify expected colors are shown

  Scenario: Search for product and verify result names and images
    Given Open amazon main page
    When Search for gaming keyboard
    Then Verify product results have name and image

