# Created by prya-prya at 10/1/19
Feature: Tests for Orders functionality

  Scenario: User must sign in to check orders
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify Sign In page is opened