@smoke
Feature: Tests for main page UI

  Scenario: Verify header in shown
    Given Open Target main page
    Then Verify header in shown

  Scenario: Verify header has correct amount links
    Given Open Target main page
    Then Verify header has 6 links
    Then Verify can click every link
