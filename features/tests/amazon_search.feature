# Created by svetlanalevinsohn at 7/29/23
Feature: Tests for amazon search

  Scenario: Verify that a user can search for a table
    Given Open Amazon page
    When Search for table
    Then Verify search result is correct

  Scenario: Verify that clicking Orders takes to signin
    Given Open Amazon page
    When Click Orders
    Then Verify sign in page opened