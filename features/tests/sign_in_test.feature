# Created by Aiza at 3/31/2024
Feature: Test sign In navigation


  Scenario: Sign In navigation
    Given Open Target.com
    When Click Sign In button
    When Click on the Sign In link from the right side navigation menu
    Then Verify Sign In form opened