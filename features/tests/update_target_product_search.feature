# created by rollyn

Feature: Update Target product search

  Scenario: User can search for product
    Given Open target main page
    When Search for product
    Then Search results for product are shown


  #  assert isinstance(context.driver.find_element(By.XPATH, "//button[@data-test='storycard--staticButton']"))
