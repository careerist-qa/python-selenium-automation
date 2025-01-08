
Feature: Logged out user can sign in

  Scenario: User can sign into target account
    Given Target main page
    When user clicks on sign in button
    When user clicks on side navigation side in button
    Then Verify if Sign in message is displayed
