# Created by prya-prya at 10/19/19
Feature: User can search for solutions of Cancelling an order on Amazon

  Scenario: User can search for solutions of Cancelling an order on Amazon
    Given Open Amazon page
    When Click on Help link
    And Input Cancel order into help search field
    And Click on Go icon
    Then Verify that Cancel Items or Orders text is present