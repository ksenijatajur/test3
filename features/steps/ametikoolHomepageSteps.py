from behave import when, then, given

from selenium.webdriver.common.by import By
import time

URL = "https://www.ametikool.ee/et"


@given("I open URL")
@when ("I open URL")
def openURL(context):
    
    context.driver.get(URL)
    

    

@then ("I check brauser URL")
def checkURL(context):
    print ("YOHOO", context)
    driver = context.driver
    print (driver.current_url)
    
    assert driver.current_url == URL
    

@then("I check menu bar")
def checkMenuBar(context):
    driver=context.driver
    avalehtMenuButton = driver.find_element(By.CSS_SELECTOR,"#header > div > div > div.header-right > div.header-right__bottom > div > ul > li:nth-child(1) > a")
    assert avalehtMenuButton.is_displayed()
    assert avalehtMenuButton.text == "Avaleht"



@when ("I search for {keyword}")
def searchFor( context, keyword):
    driver=context.driver
    searchFiled = driver.find_element(By.CSS_SELECTOR, "#edit-search-keys")
    assert searchFiled.is_displayed()
    searchFiled.send_keys(keyword)
    time.sleep(2)
    searchButton = driver.find_element(By.CSS_SELECTOR, "#edit-submit-search")
    searchButton.click()
    time.sleep(2)

@then("{keyword} is found")
def step_impl(context, keyword):
    driver=context.driver
    marksona = driver.find_element(By.CSS_SELECTOR, "#edit-keys")
    print (marksona.get_attribute('value'))
    assert keyword in marksona.get_attribute('value') 