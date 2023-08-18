# Created by ilenismosquea at 8/18/23
Feature: sign in when clicking on returns and orders

 Scenario: Verify that clicking Orders takes to signin
    Given Open Amazon page
    When Click Orders
    Then Verify sign in page opened