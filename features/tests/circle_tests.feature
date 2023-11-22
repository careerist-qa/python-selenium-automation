Feature: Target Circle tests

  Scenario: User can click through Circle tabs
    Given Open Circle page
    Then Verify that clicking though Circle tabs works

  Scenario: User is able to navigate to Google Play Target page
    Given Open Circle page
    And Store original window
    When Click Google Play button
    And Switch to new window
    Then Verify Google Play Target page opened
    And Close current page
    And Return to original window
