# created by rollyn

Feature: User can add any product to cart

    Scenario: User can add product to cart
        Given Open target main page
        When Search for tea
        And Click on add to cart button
        Then Confirm added to cart message from side navigation


