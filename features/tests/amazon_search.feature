# Created by svetlanalevinsohn at 5/6/23
Feature: Amazon Search tests

  @smoke
  Scenario: User can search for table on Amazon
    Given Open amazon main page
    When Search for table
    Then Verify search results shown for "table"

#  Scenario: User can search for coffee on Amazon
#    Given Open amazon main page
#    When Search for coffee
#    Then Verify search results shown for "coffee"

  Scenario Outline: User can search on Amazon
    Given Open amazon main page
    When Search for <search_word>
    Then Verify search results shown for <search_result>
    Examples:
    |search_word      |search_result    |
    |table            |"table"          |
    |coffee           |"coffee"         |
    |mug              |"mug"            |
    |dress            |"dress"          |

  Scenario: User can add a product to the cart
    Given Open amazon main page
    When Search for Tritan Farm to Table Pitcher
    And Click on the first product
    And Store product name
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product

  Scenario: Verify that user can see product names and images
    Given Open amazon main page
    When Search for coffee
    Then Verify that every product has a name and an image

  Scenario: Verify that user can search in a department
    Given Open amazon main page
    When Select department books
    When Search for Faust
    Then Verify correct department shown
