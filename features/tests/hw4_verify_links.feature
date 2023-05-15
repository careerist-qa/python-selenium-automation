# Created by domon at 5/15/2023
Feature: # User can see 5 links in Best Sellers Header field
  # Enter feature description here

  Scenario: # User can see 5 links
    Given Open amazon main page
    When Click best sellers button
    Then Verify 5 best sellers header links


  Scenario: # User can see different fields
    Given Open amazon main page
    When Click Customer Service button
    Then Verify Welcome to Amazon Customer Service Message
    Then Verify 10 items in container
    Then Verify search our help library message
    Then Verify customer service search box
    Then Verify all help topics message
    Then Verify 12 help topics

