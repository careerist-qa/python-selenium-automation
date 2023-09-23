# Created by jacobgrable at 9/22/23
Feature:  User needs to Sign In


  Scenario: Sign In page can be opened from SignIn popup
    Given Open Amazon Page
    When Click on button from Signin popup
    Then Verify Sign In page