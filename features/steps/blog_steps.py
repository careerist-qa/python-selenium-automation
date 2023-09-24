from behave import then


@then('Verify blog is opened')
def verify_blog_opened(context):
    context.app.blog.verify_opened()


@then('Close blog')
def close_blog(context):
    context.app.close_page()


@then('Return to original window')
def return_to_original_window(context):
    context.app.blog.switch_to_window(context.original_window)