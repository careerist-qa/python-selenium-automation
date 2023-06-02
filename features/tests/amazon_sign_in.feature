# Created by svetlanalevinsohn at 2/25/23
Feature: Amazon Sign in tests

 Scenario: User can see sign in page
   Given Open amazon main page
   When Click Orders
   Then Verify Sign In page opens

 Scenario: Sign In page can be opened from SignIn popup
   Given Open amazon main page
   When Click on button from SignIn popup
   Then Verify Sign In page opens

 Scenario: Amazon users see sign in button
   Given Open amazon main page
   Then Verify Sign In is clickable
   When Wait for 3 sec
   Then Verify Sign In is clickable
   Then Verify Sign In disappears