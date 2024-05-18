Feature: Launch and Search Python.org

Scenario: Launch Python.org
  Given we have selenium installed
   When we launch https://www.python.org in chrome
   Then we obtain title "Welcome to Python.org"

Scenario: Search Getting started in Python
  Given we have selenium installed
   When we launch https://www.python.org in chrome
    And we search "getting started in Python"
   Then we arrive at search page
    And we obtain some result