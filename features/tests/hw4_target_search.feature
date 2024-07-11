# Created by jkwak at 7/6/24
Feature: Test Case for Search Functionality
  # Enter feature description here

  Scenario: User can search for a product
    Given Open target.com
    When Input tea in input search
    And Click button search
    Then Verify tea search result is shown
    Then Verify correct search URL opens for tea


  Scenario: User can search for a product
    Given Open target.com
    When Input shoes in input search
    And Click button search
    Then Verify shoes search result is shown
    Then Verify correct search URL opens for shoes
    # Enter steps here