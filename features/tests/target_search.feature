Feature: Search tests


  Scenario: User can search for a tea
    Given Open Target main page
    When Search for icetea
    Then Verify search results are shown for icetea
    Then Verify that URL has icetea

  Scenario Outline: User can search for a product
    Given Open Target main page
    When Search for <item>
    Then Verify search results are shown for <expected_item>
    Examples:
    |item         |expected_item  |
    |mug          |mug            |
    |tea          |tea            |
    |white mug    |white mug      |
