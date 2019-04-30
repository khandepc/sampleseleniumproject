Feature: to verify create account functionality of facebook
  @home
  Scenario: create account with invalid mobile number

    Given pass first name as prashant

    Then pass sname as khande

    Then pass mobile number as 1234567890

    Then pass password as khande123

    Then select birth day as 14

    Then select birth month as sep

    Then select birth year as 1996

    Then click on gender as male

    Then click on signup button

