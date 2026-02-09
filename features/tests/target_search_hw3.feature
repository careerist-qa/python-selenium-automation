Feature: Target search test cases


##Empty cart message
  Scenario: User can verify cart is empty
    Given Open target main page
    When Click on Cart icon
    Then Verify Empty cart message is shown


## Verify log out to log in
  Scenario: Logged out User can navigate to sign in page
    Given Open target main page
    When Click Sign in
    Then Verify Sign in Form opens




