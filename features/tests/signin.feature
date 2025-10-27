# Created by Davon Gilliam at 10/11/2025
Feature: Test for Logged Out Users signing in.
  # Enter feature description here

	Scenario: User can navigate to signin page.
    Given Open the Target page
	When Click signin button
	Then Verify signin form opened