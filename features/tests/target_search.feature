# Created by svetlanalevinsohn at 3/30/24
Feature: Search tests

  Scenario: User can search for a product
    Given Open Target main page
    When Search for 'coffee'
    Then Verify search results are shown

  Scenario: User can search for tea
    Given Open Target main page
#    When Search for 'tea'
#    Then Verify search results are shown for tea