# Created by jblai at 9/15/2023
Feature: Tests for amazon search


  Scenario: Verify that a user can search for a table
    Given Open Amazon page
    When Search for table
    Then Verify search result is correct

  Scenario: open
