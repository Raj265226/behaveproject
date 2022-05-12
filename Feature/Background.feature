Feature: OrangeHRM Login

  Background: common steps
    Given  I Launch browser
    When  I open application
    And  Enter valid username and password
    And  Click on login

  Scenario:  Login to HRM Applicaion
    Then User must login to the Dashboard page

  Scenario:  Search User
    When  navigate to search page
    Then  search page should display

  Scenario: Advance search user
    When  navigate to advance search page
    Then  advance search page should display