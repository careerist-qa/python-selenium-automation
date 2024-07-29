from behave import given, when, then


@then('HW8 Pause {s} seconds at the end to review the result of step')
def pause_step(context, s):
    context.hw8app.hw8_page_base.pause_sleep(s)
