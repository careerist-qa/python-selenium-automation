Feature: Test Scenarios for Search functionality

  Scenario Outline: User can search for a product
    Given Open Google page
    When Input <search_word> into search field
    And Click on search icon
    Then Product results for <search_result> are
  Examples:
  |search_word        |search_result        |
  |car                |"car"                |
  |table              |"table"              |
  |Notebook           |"Notebook"           |
  |Saree              |"Saree"              |

  # Scenario: User can search for a product
  #  Given Open Google page
  #  When Input Table into search field
  #  And Click on search icon
  #  Then Product results for Table are shown