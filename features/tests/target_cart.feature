# Created by toshinagpure at 4/8/24
Feature: Target cart tests

  Scenario: “Your cart is empty” message is shown
    Given Open target main page
    When Click on cart icon
    Then Verify 'Your cart is empty' message is shown

  Scenario: Logged out user can navigate to Sign In
    Given Open target main page
    When Click Sign In
    When Click on sign in from right side navigation menu
    Then Verify Sign In form opened
