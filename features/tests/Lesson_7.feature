# Created by jblai at 9/28/2023
Feature: Lesson 7 implement waits

  Scenario: Verify popup button appears and disappears
    Given Open Amazon page
    When Verify Sign-in is clickable
    When wait for 3 seconds
    When Verify Sign-in is clickable
    Then Verify Sign-in disappears
