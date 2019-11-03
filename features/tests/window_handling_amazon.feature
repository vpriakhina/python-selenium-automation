# Created by prya-prya at 11/1/19
Feature: Test for window handling functionality


  Scenario: User can open and close Today's deals and add to the cart
    Given Open Amazon page
    When Store original windows
    And Click to open Deals under 25
    And Switch to the newly opened window
    Then Shop all deals are shown
    And Put any product into a cart
    And User can close new window and switch back to original
    And Refresh the page
    And Verify cart has 1 item
