# Created by 12405 at 5/23/2024
Feature: Target look at products
  # Enter feature description here

  Scenario: Target product presented
    Given Open Target page
    When Input dog into search bar
    Then Verify product names and images displays

  Scenario: Amazon bestsellers
    Given Open Amazon Bestsellers
    When Click headers
