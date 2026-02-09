Feature: Update target Page Object


Scenario: "Your cart is empty" message is shown for empty cart
  Given Open target.com
  When Click on Cart icon
  Then Verify 'Your cart is empty' message is shown