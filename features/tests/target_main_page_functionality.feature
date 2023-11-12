Feature: Target main page functionality

  Scenario: Card is empty
    Given Open Target main page
    When Click on Cart icon
    Then 'Your cart is empty' message is shown


  Scenario: User can access Sign In
    Given Open Target main page
    When Click Sign In
    And From right side navigation menu, click Sign In
    Then Verify Sign In form opened


  Scenario: User can access Sign In
    Given Open Target main page
    When Search for apple ipad 10th generation
    Then Verify search worked for apple ipad 10th generation
    And Verify apple+ipad+10th+generation in search result url