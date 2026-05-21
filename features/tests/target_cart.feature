# Created by willi at 5/4/2026
Feature: Target Cart Page
  # Enter feature description here

  ##Homework 3
  Scenario: Verify cart page is empty
    Given Open target.com
    When I click on the cart icon
    Then I should see "Your cart is empty"

## Feature: Sign In Navigation

  Scenario: Navigate to Sign In from homepage
    Given I open Target homepage
    When I click on the Sign In button
    Then the Sign In form should be displayed
