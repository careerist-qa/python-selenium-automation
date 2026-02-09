# created by rollyn
Feature: Test Scenarios for Target's Cart and Sign In Button functionality

  Scenario: User can use Target cart buttons
    Given Open target main page
    When Click on Cart Icon
    Then "Your cart is empty" message is shown


  Scenario: User can navigate to "sign In"
    Given Open target main page
    When Click on account button
    And Click on Sign In or Create Account button
    Then "Sign in or create account" page is shown