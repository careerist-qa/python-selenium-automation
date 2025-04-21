from behave import given, when, then



@given("Open Target Help Page")
def open_help_page(context):
    context.app.target_help_page.open_target_help_page()


@then("Verify Target Help Page Opened")
def verify_target_help_page_opened(context):
    context.app.target_help_page.verify_help_page_opened()


@then("Select Target topic Orders and Purchases")
def select_target_topic_orders_and_purchases(context):
    context.app.target_help_page.select_topic_target_help_page()


@then("Verify Orders and Purchases page opened")
def verify_orders_and_purchases(context):
    context.app.target_help_pageverify_orders_and_purchases_opened()


