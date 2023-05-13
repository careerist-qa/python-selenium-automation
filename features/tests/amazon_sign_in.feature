# Created by svetlanalevinsohn at 2/25/23
Feature: Amazon Sign in tests

 Scenario: User can see sign in page
   Given Open amazon main page
   When Click Orders
   Then Verify Sign In page opens