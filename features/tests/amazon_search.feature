# Created by Mosqueailenis at 7/29/23
Feature: Tests for amazon search

#  Scenario: Verify that a user can search for a table
#    Given Open Amazon page
#    When Search for table
#    Then Verify search result is "table"

#  Scenario: Verify that a user can search for a cup
#    Given Open Amazon page
#    When Search for cup
#    Then Verify search result is "cup"
#
  Scenario: Verify that a user can search for a dress
    Given Open Amazon page
    When Search for dress
    Then Verify search result is "dress"

  Scenario Outline: Verify that a user can search for a product
    Given Open Amazon page
    When Search for <search_word>
    Then Verify search result is <search_result>
    Examples:
    |search_word      |search_result    |
    |cup              |"cup"            |
    |dress            |"dress"          |
    |tea              |"tea"            |
    |coffee           |"coffee"         |
    |forks            |"forks"          |