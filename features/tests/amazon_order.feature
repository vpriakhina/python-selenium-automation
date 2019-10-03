# Created by prya-prya at 10/1/19
Feature: Test Scenario for Orders

  Scenario: User must sign in to check orders
    Given Open Amazon page
    When Click Order button
    Then Result Contains Sign-In