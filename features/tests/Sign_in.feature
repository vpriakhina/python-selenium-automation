# Created by prya-prya at 11/3/19
Feature: Test for Sign In functionality
  # Enter feature description here

  Scenario: Sign In tooltip appears and disappears
    Given Open Amazon page
    Then Verify Sign In tooltip is present and clickable
    When Wait until Sign In tooltip disappears
    Then Verify Sign In tooltip is not clickable