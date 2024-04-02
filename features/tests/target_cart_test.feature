# Created by Aiza at 3/31/2024
Feature: Verify empty cart message on Target.com


  Scenario: Verify "Your cart is empty" message when clicking on the cart icon
    Given Open Target main page
    When  Click on the Cart icon
    Then  Verify “Your cart is empty” message is shown

