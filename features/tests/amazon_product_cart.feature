Feature: Test Scenarios for Amazon add product  functionality

  Scenario: Add a product to cart and confirm selected product exist in the cart
    Given Enter Amazon page
    When Enter  product outdoor furniture in search field
    And  Click the search icon
    Then choose your product from result page
    And click add to cart button
    And confirm that selected product in the cart
