from behave import given, when, then
from time import sleep


@given('Open Amazon T&C page')
def open_amazon_tc_page(context):
    context.app.terms_condition_page.open_tc_page()

@when('Store original windows')
def store_original_windows(context):
    context.original_window = context.app.terms_condition_page.store_original_windows()



    @when('Click on Amazon Privacy Notice link')
    def click_privacy_notice(context):
        context.app.terms_condition_page.click_on_privacy_notice()
        sleep(10)

    @when('Switch to the newly opened window')
    def switch_to_new_window(context):
        context.app.base_page.switch_to_new_window()

        @then('Verify Amazon Privacy Notice page is opened')
        def verify_privacy_notice_page(context):
            context.app.terms_condition_page.verify_privacy_notice()

            @then('User can close new window and switch back to original')
            def close_new_window_switch(context):
                    context.app.base_page.close_page()
                    context.app.terms_condition_page.switch_to_window(context.original_window)

                    sleep(10)

