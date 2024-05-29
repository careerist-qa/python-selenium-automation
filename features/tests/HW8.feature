# Created by 12405 at 5/14/2024
Feature: Target help page selects
  # Enter feature description here

  Scenario: Target help dropdown
    Given Open Target help page
    When Select dropdown option
    Then Verify page is correctly changed

  Scenario:
    Given Open Target page
      When Click on sign in icon
      When Click on sign in button
      Then Verify sign in page is present
      And Enter username
      And Enter Password
      And Click on sign in
      Then Verify error message appears