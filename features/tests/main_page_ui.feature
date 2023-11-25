Feature: Main page UI tests

  Scenario: Header has correct amount of links
    Given Open target main page
    Then Verify header is present
    And Verify header has 5 links

  Scenario: User can see signin arrow
    Given Open target main page
    When Hover over signin
    Then Verify signin arrow shown