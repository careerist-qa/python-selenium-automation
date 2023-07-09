# Created by domon at 5/6/2023
Feature: Amazon Search tests

#  Scenario: User can search for table on Amazon
#    Given Open amazon main page
#    When Search for table
#    Then Verify search results shown for "table"
#
#  Scenario: User can search for coffee on Amazon
#    Given Open amazon main page
#    When Search for coffee
#    Then Verify search results shown for "coffee"

  Scenario Outline: User can search on Amazon
    Given Open amazon main page
    When Search for <search_word>
    Then Verify search results shown for <search_result>
    Examples:
    |search_word   |search_result  |
    |table         |"table"        |
    |mug           |"mug"          |
    |coffee        |"coffee"       |
    |mug           |"mug"          |



