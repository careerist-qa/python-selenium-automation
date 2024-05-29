# Created by 12405 at 5/12/2024
Feature: Amazon finds

Scenario: Logged out user sees Sign in page when clicking Orders
 Given Open Amazon page
 When Click Amazon Orders link
 Then Verify Sign in page opened

Scenario: 'Your Shopping Cart is empty' shown if no product added
 Given Open Amazon page
 When Click on cart iconA
 Then Verify "Your Shopping Cart is empty." text present