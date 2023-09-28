# Created by jblai at 9/15/2023
Feature: Tests for amazon search
  Scenario: Verify that a user can search for a dress
    Given Open Amazon page
    When Search for dress
    Then Verify search result is "dress"
#
#  Scenario Outline: Verify that a user can search for a product
#    Given Open Amazon page
#    When Search for <search_word>
#    Then Verify search result is <search_result>
#    Examples:
#    |search_word     |search_result    |
#    |cup             |"cup"            |
#    |dress           |"dress"          |
#    |table           |"table"          |
#

