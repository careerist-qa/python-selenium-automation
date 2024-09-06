# Created by lana at 9/5/24
Feature: Tests for Target Search functionality

  Scenario: User can search for a product
    Given Open target main page
    When Search for a product
    Then Verify that correct search results shown

  Scenario: User can search for a product2
    Given Open target main page
#    When Search for a product
#    Then Verify that correct search results shown

#  Scenario: User can see Cart Empty message
#    Given Open target main page
#    When Click on cart icon
#    Then Verify cart Empty message shown
