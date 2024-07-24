# Created by jkwak at 7/23/24
Feature: Add a product to cart
  # Test functions used in adding a product to cart

  Scenario: Verify Sign In form opened
    # When clicking Sign In button, the form should be opened
    Given HW7 Open the main page
    When HW7 Click the sign-in link
    Then HW7 Verify the sign-in form opened


  Scenario: User can log in using Page Object pattern
    #Create a login test case using Page Object pattern
    Given HW7 Open the main page
    When HW7 Click the sign-in link
      And HW7 Input email and password on SignIn page
      And Click on Sign in on SignIn page
    Then Verify user is logged in (sign in form should disappear)


