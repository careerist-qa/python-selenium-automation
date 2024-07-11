# Created by jkwak at 7/8/24
Feature: Test Cases for Help Page UI Elements
  # Enter feature description here

  Scenario: All UI elements should be present of Help page
    Given Open target.com
    When Open Help page
    Then Verify 6 UI elements are present of the page
