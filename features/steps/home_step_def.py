from behave import given,when,then
import generic.seleniumbase as sb
import pageobjects.fbhomepage as fbhomepage


@given(u'pass first name as {value}')
def step_impl(context, value):
    element=fbhomepage.get_fname_element()
    sb.perform_action(element,"settext",value)

@then(u'pass surname as {value}')
def step_impl(context,value):
    element = fbhomepage.get_sname_element()
    sb.perform_action(element, "settext", value)

@then(u'pass mobile number as {value}')
def step_impl(context,value):
    element = fbhomepage.get_mobile_email_element()
    sb.perform_action(element, "settext", value)


@then(u'pass password as {value}')
def step_impl(context,value):
    element = fbhomepage.get_password_element()
    sb.perform_action(element, "settext", value)


@then(u'select birthday date as {value}')
def step_impl(context,value):
    element=fbhomepage.get_birth_day_element()
    sb.perform_action(element,"select",value)

@then(u'select birthday month as {value}')
def step_impl(context,value):
    element = fbhomepage.get_birth_month_element()
    sb.perform_action(element,"select",value)


@then(u'select birthday year as {value}')
def step_impl(context,value):
    element = fbhomepage.get_birth_year_element()
    sb.perform_action(element,"select",value)


@then(u'click on gender as {value}')
def step_impl(context,value):
    element=fbhomepage.get_gender_element()
    sb.perform_action(element,"click")

@then(u'click on sign up button')
def step_impl(context):
    element = fbhomepage.get_signup_button_element()
    sb.perform_action(element,"click")
