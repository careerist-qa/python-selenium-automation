# Created by jkwak at 7/8/24
Feature: Test Cases for Target Circle Page
  # Test the target circle page has all correct links

  Scenario: Open the Target Circle page
    Given Open target.com
    When Open the target circle page
    Then Verify there are 10 benefit cells
