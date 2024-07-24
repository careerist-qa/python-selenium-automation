from behave import given, when, then


@when('HW7 Save the product title')
def save_the_product_title(context):
    context.added_product_title = context.hw7app.hw7_page_product.save_the_product_title()
    print(f'added_product_title in product step: {context.added_product_title}')


@when('HW7 Click on Add to Cart button')
def click_add_to_cart_and_save_product_name(context):
    context.hw7app.hw7_page_product.add_the_product_to_cart()


@when('HW7 Click View cart & check out')
def click_view_cart_and_checkout(context):
    context.hw7app.hw7_page_product.view_cart_and_checkout()