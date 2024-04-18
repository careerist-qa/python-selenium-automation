Feature: Add Product

  Scenario: User can add a product to cart
    Given Open Target main page
    When Search for mug
    And Click on Add to Cart button
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product



