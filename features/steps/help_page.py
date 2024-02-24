from behave import given, when, then


@given('Open Help page for Returns')
def open_target_help_returns(context):
    context.app.help_page.open_help_returns()


@when('Select Help topic {help_topic}')
def select_promotions(context, help_topic):
    context.app.help_page.select_topic(help_topic)


# @then('Verify Returns page opened')
# def verify_returns_opened(context):
#     context.app.help_page.verify_returns_opened()
#
#
# @then('Verify Current promotions page opened')
# def verify_promotions_opened(context):
#     context.app.help_page.verify_promotions_opened()


@then('Verify {expected_header} page opened')
def verify_promotions_opened(context, expected_header):
    context.app.help_page.verify_header(expected_header)
