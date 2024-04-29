# Created by toshinagpure at 4/6/24
Feature: Search tests

  Scenario: User can search for coffee
    Given Open target main page
    When Search for 'coffee'
    Then Verify search results are shown for coffee

  Scenario: User can search for tea
    Given Open target main page
    When Search for 'tea'
    Then Verify search results are shown for tea

  Scenario Outline: User can search for product
    Given Open target main page
    When Search for '<item>'
    Then Verify search results are shown for <expected_item>
    Examples:
    |item    |expected_item  |
    |sugar   |sugar          |
    |spoon   |spoon          |
    |coffee  |coffee         |
    |tea     |tea            |


  Scenario: Verify that user can see product name and images
    Given Open target main page
    When Search for 'moisturizer'
    Then Verify that every product has a name and an image
