# Created by prya-prya at 11/2/19
Feature: Test for top menu functionality


  Scenario: User can loop through top menu
    Given Open Amazon page
    When Click Best Sellers link
    Then Verify user can loop through top menu
