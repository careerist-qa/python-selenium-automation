Feature: Cart tests

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown

  @smoke
  Scenario: User can add a product to cart
    Given Open target main page
    When Search for Lunar New Year M&M's
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product

  Scenario: User can add different products to cart
    Given Open target main page
    When Search for Lunar New Year M&M's
    And Click on Add to Cart button for product 1
    And Store product name to a list
    And Confirm Add to Cart button from side navigation
    And Close side navigation
    And Click on Add to Cart button for product 2
    And Store product name to a list
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 2 item(s)
    And Verify cart has correct multiple products