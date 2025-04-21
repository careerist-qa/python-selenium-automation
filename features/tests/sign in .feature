
Feature: Sign In

  Scenario: User can sign into target account
    Given Target main page
    When user clicks on sign in button
    When user clicks on side navigation side in button
    Then Verify if Sign in message is displayed

Scenario: User cannot sign in with incorrect password
  Given Open Target page
  When user clicks on sign in button
  And user clicks on side navigation side in button
  And user inputs correct email address
  And User clicks continue button
  When user enters incorrect password
  And Clicks sign in with password
  Then Verify error message is shown


