# Created by prya-prya at 10/19/19
Feature: Test for hamburger menu functionality

  Scenario: Amazon Music has 6 menu items
    Given Open Amazon page
    When Click on hamburger menu
    And Click on Amazon Music menu item
    Then 6 menu items are present

