from generic import seleniumbase as sb

id_fname="u_0_j"
id_sname="u_0_l"
id_mobile_email="u_0_o"
id_password="u_0_v"
id_birth_day="day"
id_birth_month="month"
id_birth_year="year"
xpath_gender="//label[contains(text(),'%s')]/preceding-sibling::input"
name_signup_button="websubmit"


def get_fname_element():
    return sb.get_element("id",id_fname)

def get_sname_element():
    return sb.get_element("id",id_sname)

def get_mobile_email_element():
    return sb.get_element("id",id_mobile_email)

def get_password_element():
    return sb.get_element("id",id_password)

def get_birth_day_element():
    return sb.get_element("id",id_birth_day)

def get_birth_month_element():
    return sb.get_element("id",id_birth_month)

def get_birth_year_element():
    return sb.get_element("id",id_birth_year)

def get_gender_element():
    return sb.get_element("xpath",xpath_gender)

def get_signup_button_element():
    return sb.get_element("name",name_signup_button)