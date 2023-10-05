from behave import *


@then('verify blog opened')
def verify_blog_opened(context):
    context.app.blog.verify_opened()

@then('Close Blog')
def close_blog(context):
    context.app.blog.close_page()

@then('Return to original window')
def return_to_original_window(context):
    context.app.blog.switch_to_window(context.original_window)
