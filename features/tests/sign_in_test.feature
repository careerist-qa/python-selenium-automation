Feature: Target Sign In

  Scenario: Logged out user can Sign in
    Given Open Target main page
    When  Click Sign in
    Then From side nav menu, click Sign in
    And Verify Sign in form opened