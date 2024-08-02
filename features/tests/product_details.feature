Feature: Tests for product page

  @smoke
  Scenario: User can select colors
    Given Open target product A-54551690 page
    Then Verify user can click through colors
