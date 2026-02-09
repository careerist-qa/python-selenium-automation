# created by rollyn
Feature: Test Scenarios for Target's Circle functionality

  Scenario: User can use benefit cells
    Given Open target main page
    When Open target circle
    And Click for benefit cells
    Then Sign in or create account page

  Scenario: User can use the pharmacy button
    Given Open target main page
    When Open target circle
    And Click for pharmacy
    Then CVS Pharmacy & Vaccines page


  Scenario: User can use the target help button
    Given Open target main page
    When Open target circle
    And Click for target help
    Then Verify the help page opens