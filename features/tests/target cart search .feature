
Feature: Adding products to Target cart


  Scenario: User can add a product into target cart
    Given Open Target page
    When Click on Categories
    When Click on Christmas button
    When Click on Christmas Deals
    When Click on Christmas Trees
    When Click on first christmas tree
    When Click on Add to cart
    When Click on view cart and checkout button
    Then Verify if result is shown

