Feature: Update Target search test cases and add Behave variables


##Search for color of product, click each color, verify color selected
  Scenario: Add product to cart
    Given Open target product {men-s-soft-knit-johnny-collar-polo-sweater-goodfellow-co/-/A-94329580?preselect=94405482#lnk=sametab} page
    Then Click through colors and verify selection
