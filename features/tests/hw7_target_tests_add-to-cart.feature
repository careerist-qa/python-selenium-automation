# Created by jkwak at 7/23/24
Feature: Test Cases for Add To Cart Functionality by Page Object pattern
  # Enter feature description here

  Scenario Outline: User can add a product to cart
    Given HW7 Open the main page
    When HW7 Search for <product>
      And HW7 Open the first product page
      And HW7 Save the product title
      And HW7 Click on Add to Cart button
      And HW7 Click View cart & check out
    Then HW7 Verify cart has <amount> item(s)
      And HW7 Verify cart has correct product
    Examples:
    | product | amount |
    | mug     | 1      |

