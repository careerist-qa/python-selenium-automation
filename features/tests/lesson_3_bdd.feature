# Created by jacobgrable at 9/17/23
Feature: User can sign in into amazon from returns and orders
  # Enter feature description here

  Scenario: User Needs to sign into Amazon
    Given Open Amazon Page
    When Click on Returns and Orders
    Then Taken to Sign In page
