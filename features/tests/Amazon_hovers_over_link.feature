Feature: Test Scenarios for Amazon mouse hover over the link functionality

  Scenario: Verify that the user can see the deals
    Given Enter Amazon product page
    When Mouse hover over NewArrivals
    Then confirm that men deal is shown
