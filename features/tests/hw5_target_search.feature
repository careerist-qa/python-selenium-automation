# Created by jkwak at 7/17/24

Feature: Test Case for Search Functionality
  # Enter feature description here

  Scenario: User can search for a product
    Given Open target main page
    When Search for tea
    Then Verify all tea search results