# Created by domon at 5/7/2023
Feature: Verify Empty Cart


  Scenario: User Should See Empty Cart After Opening Amazon
    Given Open amazon main page
    When Click on cart button
    Then User can see empty cart message