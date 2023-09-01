Feature: sigin tests homework

  Scenario: Verify that clicking Orders takes to signin
    Given Open Amazon page
    When Click Amazon Orders
    Then Verify sign in page opened

Scenario: Sign In page can be opened from SignIn popup
    Given Open Amazon page
    When Click on button from SignIn popup
    Then Verify sign in page opened