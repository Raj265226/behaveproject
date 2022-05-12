from behave import *
from selenium import webdriver

@given('I launch chrome browser')
def Launch_Browser(context):
    context.driver=webdriver.Chrome(executable_path="E:\Work Files\Webdrives_for_Automation\chromedriver.exe")


@when('I Open orange hrm homepage')
def OpenHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "{user}" and password "{pwd}"')
def EnterUserPwd(context,user,pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)


@when('Click on login button')
def LoginButton(context):
    context.driver.find_element_by_id("btnLogin").click()


@then('User must successfully login to the dashboard page')
def DashboardPage(context):
    try:
        text=context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    except:
        context.driver.close()
        assert  False,"Test Failed"
    if text=="Dashboard":
        context.driver.close()
        assert True,"Test Passed"
