from os import link

from behave import given,when,then
from numpy.testing import assert_equal


@given(u'The user accesses the page https://qavbox.github.io/demo/dragndrop/')
def step_impl(context):
    context.dd.setup(link)


@when(u'The user move the"Drag me to my target" into the droppable element on the home page')
def step_impl(context):
    context.dd.drag()

@then(u'The message "Dropped" is displayed')
def step_impl(context):
    context.dd.drop()
    msg = context.dd.drop()
    assert_equal(msg, "Dropped!")
