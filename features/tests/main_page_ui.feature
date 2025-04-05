Feature: Main page UI test

  Scenario: Verify header links has at least 1 link
    Given Open target main page
    Then Verify at least 1 link shown

  Scenario: Verify all header links shown
    Given Open target main page
    Then Verify 6 links shown

    Feature: Verify Target Circle Benefits

  Scenario: Verify benefit cells on the Target Circle page
    Given Open the Target Circle page
    Then Verify there are at least 10 benefit cells