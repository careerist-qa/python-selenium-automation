## Created by jblai at 9/15/2023
Feature: Check order page


  Scenario: Open Sign-in page via orders button
    Given Open Amazon Page
    When Click Amazon Orders link
    Then Verify Sign-in page is opened

  Scenario: Open Sign-in page via popup button
    Given Open Amazon Page
    When Click on button from Sign-In popup
    Then Verify Sign-in page is opened

  Scenario: Open Cart and verify that cart is empty
    Given Open Amazon page
    When Click Cart
    Then Verify cart is Empty
