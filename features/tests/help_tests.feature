Feature: Tests for Help pages

  Scenario: User can select Help topic
    Given Open Help page for Returns
    Then Verify Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify Current promotions page opened

  Scenario: User can select Help topic Target Circle
    Given Open Help page for Returns
    Then Verify Returns page opened
    When Select Help topic Target Circle™
    Then Verify About Target Circle page opened