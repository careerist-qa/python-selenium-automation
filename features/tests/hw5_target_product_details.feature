# Created by jkwak at 7/17/24
Feature: Test Cases for Selections on Product Details
  # Enter feature description here

  Scenario Outline: User can use color selection for a product
    Given Open target product <product_id> page
    Then Verify user can click through <colors>
    Examples:
    |product_id | colors                                         |
    |A-91511634 | ['dark khaki', 'stone/grey', 'black/gum']      |
    |A-54551690 | ['Blue Tint', 'Denim Blue', 'Marine', 'Raven'] |