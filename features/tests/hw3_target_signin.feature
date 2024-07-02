# Created by jkwak at 7/2/24
Feature: Test Scenario for Sign In Functionality
  # verify Sign In form open when clicking on Sign In icon

  Scenario: User can open Sign In form
    Given Open target.com
    When Click on Sign In icon
    When Click on Sign In from right side menu
    Then Verify Sign In form opened