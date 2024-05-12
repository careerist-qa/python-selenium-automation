# Created by 12405 at 5/3/2024
Feature: Target Functions
  # Enter feature description here

  Scenario: Target item search
    Given Open Target site
    When Input cup into search bar
    Then Item results for for “cup” are displayed

  Scenario: Target Benefit Cells
    Given Open Target benefit page
    Then 10 Benefit cells populate

  Scenario: Target item search
    Given Open Target site
    When Input cup into search bar
    Then Item results for for “cup” are displayed
    When Add any item to cart
    When Go to cart
    Then Verify an item is in cart
