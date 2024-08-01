# Created by jkwak at 7/24/24
Feature: Terms and Conditions Page Test
  # function test for Terms and Conditions page

  Scenario Outline: User can open and close Terms and Conditions from sign in page
    Given HW8 Open sign in page
    When HW8 Store original window
    And HW8 Click on Target terms and conditions link
    And HW8 Switch to the newly opened window
    Then HW8 Verify Terms and Conditions page is opened
    And HW8 User can close new window and switch back to original
#   For reliability test purpose with 5 times
    Examples:
    | time |
    | 2    |
#    | 2    |
#    | 2    |
#    | 2    |
#    | 2    |
