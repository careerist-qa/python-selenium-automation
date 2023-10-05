# Created by jblai at 10/3/2023
Feature:  Tests for 404 page
  Scenario: user is able to navigate to amazon blog form 404 page
    Given Open Amazon product 807NF5WGQ11111111111 page
    And Store original window
    When Click on a dog image
    And Switch to a new window
    Then Verify blog opened
    And Close blog
    And Return to original window