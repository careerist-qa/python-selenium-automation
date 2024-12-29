Feature: Cart Empty

Scenario: “Your cart is empty” message is shown for empty cart
  Given Target main page
  When Click on Cart icon
  Then Verify “Your cart is empty” message is shown
