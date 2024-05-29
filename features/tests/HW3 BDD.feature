# Created by 12405 at 5/1/2024
Feature: Target HW3

  Scenario: Target cart check
    Given Open Target page
    When Click on cart icon
    Then Verify cart page is present

  Scenario: Target sign in page
    Given Open Target page
    When Click on sign in icon
    When Click on sign in button
    Then Verify sign in page is present