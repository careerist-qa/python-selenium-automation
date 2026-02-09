# created by rollyn
  Feature: Rewrite this scenario with Page Object pattern:

    Scenario: "Your cart is empty" message is shown for empty cart
      Given Open target main page
      When Click on Cart Icon
      Then "Your cart is empty" message is shown