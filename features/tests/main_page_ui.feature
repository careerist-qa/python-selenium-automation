Feature: Tests for main page UI

  Scenario: Verify header in shown
    Given Open Target main page
    Then Verify header in shown

  Scenario: Verify header has correct amount links
    Given Open Target main page
    Then Verify header has 5 links

  Scenario: User can see signin arrow
    Given Open target main page
    When Hover over signin
    Then Verify signin arrow shown