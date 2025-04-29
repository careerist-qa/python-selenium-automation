Feature: Tests for main page UI

  Scenario: Verify header in shown
    Given Open Target main page
    Then Verify header is shown

  Scenario: Verify header has correct amount links
    Given Open Target main page
    Then Verify header is shown
    And Verify header has 6 links