from os import link

from behave import given,when,then
from numpy.testing import assert_equal
from selenium.webdriver import ActionChains


@when(u'The user scrolls the sidebar up to 100')
def step_impl(context):

    context.dd.slide()
@then(u'The range 100 is displayed')
def step_impl(context):

    context.dd.message()
