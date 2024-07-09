Feature: Sign in Navigation functionality

  Scenario: Logged out users can navigate to Sign in
    Given Open Target main page
    When Clicking on Sign in
    Then Verify Sign in form opens