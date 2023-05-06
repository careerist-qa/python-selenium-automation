# Created by svetlanalevinsohn at 5/6/23
Feature: Amazon Search tests

  Scenario: User can search for table on Amazon
    Given Open amazon main page
    When Search for table
    Then Verify search results shown for "table"

  Scenario: User can search for coffee on Amazon
    Given Open amazon main page
    When Search for coffee
    Then Verify search results shown for "coffee"
