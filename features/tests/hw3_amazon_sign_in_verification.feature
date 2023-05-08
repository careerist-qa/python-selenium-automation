# Created by domon at 5/6/2023
Feature: Verify User Can Login from Cart Button

  Scenario: Logged Out User can see sign-in page from clicking Cart
    Given Open amazon main page
    When Clicks on orders button
    Then User can see sign-in page