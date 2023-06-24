Feature: Test Scenarios for drop down functionality

  Scenario: Verify that search for an item in a different amazon department
    Given Enter Amazon web page
    When choose the department search-alias=appliances in department section
    Then enter item drip bowls for electric stove search field
    And  press the search icon
    And confirming given product result page brought from selected Appliances

