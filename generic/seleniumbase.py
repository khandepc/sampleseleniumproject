from selenium import webdriver
from selenium.webdriver.support import select
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as ec
from time import*
from selenium.webdriver.common.action_chains import ActionChains
# to launch app

def launch_app(browser_name, url):
    global driver
    print(browser_name, end ='')
    if browser_name == 'chrome':
        chromeoptions = webdriver.ChromeOptions()
        chromeoptions.add_argument("start-maximized")
        chromeoptions.add_argument("--ignore-cetrificate-errors")
        chromeoptions.add_argument("disable-notifications")
        chromeoptions.add_argument("--disable-infobars")
        chromeoptions.add_argument("--disable-extensions")
        driver = webdriver.Chrome(executable_path='./drivers/chromedriver.exe', options=chromeoptions)
    elif browser_name == "firefox":
        pass
    elif browser_name == "ie":
        pass
    else:
        print("incorrect browser name")
    # to get url
    driver.get(url)


# to close the browser
def close_app():
    driver.quit()


# to find element

def get_element(locater_type, locater):
    element = None
    if locater_type == "id":
        return driver.find_element_by_id(locater)
    elif locater_type == "name":
        return driver.find_element_by_name(locater)
    elif locater_type == "classname":
        return driver.find_element_by_class_name(locater)
    elif locater_type == "tagname":
        return driver.find_element_by_tag_name(locater)
    elif locater_type == "css":
        return driver.find_element_by_css_selector(locater)
    elif locater_type == "xpath":
        return driver.find_element_by_xpath(locater)
    elif locater_type == "linktext":
        return driver.find_element_by_link_text(locater)
    elif locater_type == "partiallinktext":
        return driver.find_element_by_partial_link_text(locater)
    else:
        print("invalid locater type")


def identify_elements(locater_type, locater):
    elements = None
    if locater_type == "id":
        return driver.find_elements_by_id(locater)
    elif locater_type == "name":
        return driver.find_elements_by_name(locater)
    elif locater_type == "classname":
        return driver.find_elements_by_class_name(locater)
    elif locater_type == "tagname":
        return driver.find_elements_by_tag_name(locater)
    elif locater_type == "css":
        return driver.find_elements_by_css_selector(locater)
    elif locater_type == "xpath":
        return driver.find_elements_by_xpath(locater)
    elif locater_type == "linktext":
        return driver.find_elements_by_link_text(locater)
    elif locater_type == "partiallinktext":
        return driver.find_elements_by_partial_link_text(locater)
    else:
        print("invalid locater type")


def get_page_details(detail_type):
    if detail_type == "title":
        return driver.title
    elif detail_type=="url":
        return driver.current_url
    elif detail_type=="windowcount":
        return len(driver.window_handles)


def switch_to_another_window():
    parent_handle=driver.current_window_handle
    all_handles=driver.window_handles

    for handle in all_handles:
        if parent_handle != handle:

            driver.switch_to.window(handle)
            driver.maximize_window()
            break


def perform_action(element, action_type, value=None):
    if action_type == "click":
        element.click(value)
    elif action_type == "settext":
        element.send_keys(value)
    elif action_type == "select":
        element = select.Select(element)
        element.select_by_visible_text(value)

    else:
        print("action_type is unknown")

def perform_mouse_keyboard_action(action_type,value=None,source_element=None,dest_element=None,):
    ac=ActionChains(driver)
    if action_type=="click":
        ac.click(source_element)
    elif action_type=="right_click":
        ac.context_click(source_element)
    elif action_type=="drag_drop":
        ac.drag_and_drop(source_element,dest_element)
    elif action_type=="move_to_element":
        ac.move_to_element(source_element)
    elif action_type=="click_and_hold":
        ac.click_and_hold(source_element)
    elif action_type=="key_down":
        ac.key_down(value,source_element)
    elif action_type=="key_up":
        ac.key_up(value,source_element)
    elif action_type=="double_click":
        ac.double_click(source_element)
    ac.perform()

def capture_screen_shot(file_name):
    driver.save_screenshot('./reports/screenshots'+file_name+'.png')


def switch_to_iframe(element,parent=False):
    if parent:
        driver.switch_to.parent_frame()
    else:
        driver.switch_to.frame(element)

