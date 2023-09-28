# Created by jblai at 9/28/2023
Feature: Homework 6 Page Object pattern

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify Sign-In page is opened
