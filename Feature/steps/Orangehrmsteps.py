from behave import *
from selenium import webdriver
@given(u'launch chrome browser')
def launchBrowser(context):
    context.driver=webdriver.Chrome(executable_path="E:\Work Files\Webdrives_for_Automation\chromedriver.exe")


@when(u'open orange hrm homepage')
def openHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then(u'verify that the logo present on page')
def verifylogo(context):
    status=context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
    assert status is True


@then(u'close browser')
def closeBrowser(context):
    context.driver.close()
