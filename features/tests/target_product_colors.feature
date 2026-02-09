# created by rollyn
#from behave.model import Scenario

Feature: Test Scenarios for Target's products name and images


Scenario: Verify user can see product name and images
    Given Open target product A-94089062 page
    Then Verify that every product color is clicked and correct

