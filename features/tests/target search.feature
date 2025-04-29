Feature: Target search page

  Scenario Outline: User can search for a product
    Given Open Target page
    When search for a <product>
    Then verify search for results are shown for <product>
    Examples:
    | product |
    | coffee  |
    | mug     |
    | tea     |


