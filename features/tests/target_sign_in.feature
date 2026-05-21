# Created by willi at 5/21/2026
Feature: Target Cart Page
  # Enter feature description here

  ##Homework 7
  Scenario: Add a product to cart
    Given Open target.com
    When I click on the cart icon
    Then I should see "Add a product to cart"

## Feature: Sign In Navigation

  Scenario: Navigate to Sign In from homepage
    Given I open Target homepage
    When I click on the Sign In button
    Then the Sign In form should be displayed