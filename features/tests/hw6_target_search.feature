# Created by jkwak at 7/22/24

Feature: Test Case for Search Functionality by Page Objects
  # Search a product by using Page Objects

  Scenario: User can search for a product by Page
    Given Open target main page by Page
    When Search input for coffee by Page
    Then Verify coffee search results by Page