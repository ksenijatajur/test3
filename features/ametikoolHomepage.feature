Feature: homepage

Scenario: homepage is opened 
    When I open URL
    Then I check brauser URL
  #  And I check menu bar

  Scenario: homepage
    When I open URL
    Then I check menu bar

Scenario: search testimine
    Given I open URL
    When I search for testimine
    Then testimine is found