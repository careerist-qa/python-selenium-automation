# Created by jacobgrable at 9/22/23
Feature:User Sees 5 links on Best Sellers Page
  # Enter feature description here

  Scenario: User Goes to Best Sellers page
  Given Open Amazon Page
  Then Click on Best Sellers Page
  Then Verify there are 5 links
    # Enter steps here