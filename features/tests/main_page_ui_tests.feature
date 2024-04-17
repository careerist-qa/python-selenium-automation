# Created by toshinagpure at 4/15/24
Feature: Tests for main page UI


  Scenario: Verify header in shown
    Given Open target main page
    Then Verify header in shown

  Scenario: Verify header has correct amount links
    Given Open target main page
    Then Verify header has 5 links

