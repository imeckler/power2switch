from selenium import webdriver
from string import ascii_letters, digits
from random import choice
from time import sleep

alphanums = ascii_letters + digits

def random_alphanum(length):
    return ''.join(choice(alphanums) for x in xrange(length))

driver = webdriver.Firefox()

# First page
driver.get('http://staging.power2switch.com/')

zip_code_box = driver.find_element_by_name('zipcode')
zip_code_box.click()
zip_code_box.clear()
zip_code_box.send_keys('60626\n')

offer_link = driver.find_element_by_xpath(
    "//img[@alt='Champion Energy']"
    "/ancestor::div[@class='min-item']"
    "/div[@class='main-info']/a")
offer_link.click()

# Second page
def get_input_box(box_name):
    global driver
    return driver.find_element_by_xpath("//input[@id='id_{0}']".format(box_name))

def fill_forms(form_dict):
    for box_name, box_val in form_dict.iteritems():
        box = get_input_box(box_name)
        box.send_keys(box_val)

username = random_alphanum(10)
password = random_alphanum(10)
main_form_dict = {'first_name':       'John',
                  'last_name':        'Smith',
                  'email':            'john@example.com',
                  'email_confirm':    'john@example.com',
                  'phone':            '5555555555',
                  'address':          '123 Fake Street',
                  'username':         username,
                  'password':         password,
                  'password_confirm': password
                 }

fill_forms(main_form_dict)

curr_provider_opt = driver.find_element_by_xpath(
    "//span[@class='jquery-selectbox-item value-None item-2']")

curr_provider_menu_open = curr_provider_opt.find_element_by_xpath(
    "../../div[@class='jquery-selectbox-moreButton']")

curr_provider_menu_open.click()
sleep(1) # Necessary to sleep since the menu takes time to open
curr_provider_opt.click()

continue_button = driver.find_element_by_xpath("//input[@id='continue_button']")
continue_button.click()

# Third page
tos_form_dict = {'agree_initials': 'JS',
                 'birth_date':     '12/31/1963'}

fill_forms(tos_form_dict)

check_box = driver.find_element_by_xpath("//ul[@class='custom-checks']/li")
check_box.click()

how_i_heard_opt = driver.find_element_by_xpath(
    "//span[@class='jquery-selectbox-item value-Other item-8']")

how_i_heard_menu_open = how_i_heard_opt.find_element_by_xpath(
    "../../div[@class='jquery-selectbox-moreButton']")

how_i_heard_menu_open.click()
sleep(2) # Necessary to sleep since the menu takes time to open
how_i_heard_opt.click()

submit_button = driver.find_element_by_xpath("//input[@class='submit']")
submit_button.click()
