# Created by willi at 5/4/2026
Feature: Target product search
  # Enter feature description here

  ##Homework 4
  Scenario:  Search for a product using Behave variables
    Given I open Target homepage
    When I search for a product
    Then I should see search results related to the product

 Feature: Target Circle page

  Scenario: Verify storycards under Unlock added value
    Given I open the Target Circle page
    Then I should see 2 storycards under Unlock added value

Feature: Add product to cart

  Scenario: Add a product and verify cart
    Given I open Target homepage
    When I search for a product
    And I add the first product to the cart
    Then the product should appear in the cart