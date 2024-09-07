Feature: Cart tests

  Scenario: User can see Cart Empty message
    Given Open target main page
    When Click on cart icon
    Then Verify Cart Empty message shown