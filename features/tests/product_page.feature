# Created by prya-prya at 11/16/19
Feature: Test for product page

  Scenario: Size tooltip shown upon hovering over Add to Cart button
    Given Open Amazon product B074TBCSC8 page
    When Hover over Add to Cart button
    Then Verify size selection tooltip is shown

   Scenario: Deals are shown upon hovering over Sales and Deals button
    Given Open Amazon product B074TBCSC8 page
    When Hover over Sales and Deals button
    Then Verify user sees the deals

   Scenario: User can select Books department
    Given Open Amazon page
    When Select Books department
    And Search for Faust
    Then Books department is selected

  Scenario: User can select Electronics department
    Given Open Amazon page
    When Select Electronics department
    And Search for Headphones
    Then Electronics department is selected





