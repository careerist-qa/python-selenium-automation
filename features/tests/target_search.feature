Feature: Search tests

Scenario: User can search for  tea
    Given Open Target main page
    When Search for 'tea'
    Then Verify search results are shown for tea


 Scenario Outline: User can search for a product#  Given Open Target main page
    Given Open Target main page
    When Search for '<item>'
    Then Verify search results are shown for <expected_item>
    Examples:
    | item      | expected_item |
    | mug       | mug           |
    | tea       | tea           |
    | spoon     | spoon         |
    | sugar     | sugar         |

 Scenario Verify that user can see product