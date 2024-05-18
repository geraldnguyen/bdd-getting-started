from behave import *
from selenium.webdriver.common.by import By


@given('we have selenium installed')
def step_impl(context):
    assert hasattr(context, 'browser')
@when('we launch https://www.python.org in chrome')
def step_impl(context):
    context.browser.get("https://www.python.org")

@then('we obtain title "Welcome to Python.org"')
def step_impl(context):
    assert context.browser.title == "Welcome to Python.org"

@when('we search "getting started in Python"')
def step_impl(contex):
    browser = contex.browser
    search_input_field = browser.find_element(By.ID, "id-search-field")
    search_input_field.clear()
    search_input_field.send_keys("getting started in Python")

    search_go_button = browser.find_element(By.ID, "submit")
    search_go_button.click()

@then('we arrive at search page')
def step_impl(context):
    assert context.browser.current_url == "https://www.python.org/search/?q=getting+started+in+Python&submit="

@then('we obtain some result')
def step_impl(context):
    results = context.browser.find_elements(By.CSS_SELECTOR, ".list-recent-events li")
    assert  len(results) > 0
