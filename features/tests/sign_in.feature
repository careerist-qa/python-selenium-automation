# Created by LOPA at 9/17/2024
Feature: Test for Sign in functionality


  Scenario: User can see Sign into your Target account text is shown
    Given Open target main page
    When Click Sign in
    When From right side navigation menu, click Sign in
    Then Verify Sign into your Target account text is shown