# Created by prya-prya at 10/19/19
Feature: Test for Amazon Search functionality
  # Enter feature description here

  Scenario: User can search for a product
    Given Open Amazon page
    When Search for dress
    Then Search results for dress is shown

  Scenario: User can add product into the cart
    Given Open Amazon page
    When Search for green tea
    And Open the first product search result
    And Click Add on cart button
    And Close suggestion side section
    Then Verify cart has 1 item