## TC_This script  allows the user to test the Temperature conversion calcualtor 
## TC_ Allow user to choose the input and output temperature units from a list and performs the conversion accordingly. It also includes error handling when invalid input values entered and through warning message.
##Selenium code- Test case Check


import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class TestTemperatureConverter(unittest.TestCase):
  def setUp(self):
##Intialize the WebDriver (ChromeDriver)
    self.driver = webdriver.Chrome(executable_path="path/to/chromedriver")
# Open the temperature calculator web application
    self.driver.get("https://www.calculator.net/conversion-calculator.html")

try:
    # Locate input and Output elements as unit selection inside From and To List ("from-unit" and "to-unit")
    dropdown = Select(driver.find_element_by_id("from-dropdown"))
    dropdown.select_by_visible_text("from-unit")
    dropdown = Select(driver.find_element_by_id("to-dropdown"))
    dropdown.select_by_visible_text("to-unit")
  
    celsius_input = driver.find_element_by_id("celsius")
    Kelvin_input = driver.find_elemenr_by_id("Kelvin")
    fahrenheit_input = driver.find_element_by_id("fahrenheit")


##The test_invalid_input method tests an invalid input (example - "jhfhr212ha") and checks if the error message is displayed.

  def test_invalid_input(self):
        temperature_input = self.driver.find_element_by_id("value")
        error_message = self.driver.find_element_by_id("error-message")

        temperature_input.clear()
        temperature_input.send_keys("jhfhr212ha")
       

        error_message_text = error_message.get_attribute("innerText")
        self(error_message_text, "Please Provide a Valid Number!")


  def test_celsius_to_fahrenheit_conversion(self):
        from_unit = Select(self.driver.find_element_by_id("from-unit"))
        to_unit = Select(this.driver.find_element_by_id("to-unit"))
        value_input = self.driver.find_element_by_id("value")
        result = self.driver.find_element_by_id("result")

        ## Select "Celsius" as the "From" unit
        from_unit.select_by_value("Celsius")

        ## Select "Fahrenheit" as the "To" unit
        to_unit.select_by_value("Fahrenheit")

        ## Enter a value (e.g., "30")
        value_input.clear()
        value_input.send_keys("30")

        ## Trigger conversion by selecting options from "From" and "To" lists
        from_unit.select_by_value("celsius")
        value_input.click()

        ## Wait for the conversion to occur (since the application has no submit button, so wait for a moment)
        self.driver.implicitly_wait(1)

        ## Get the result
        conversion_result = result.get_attribute("value")

        ## Check the conversion result
        self.assertEqual(conversion_result, "303.15", "Celcius to Fahrenheit conversion is incorrect")

def test_fahrenheit_to_celsius_conversion(self):
        from_unit = Select(self.driver.find_element_by_id("from-unit"))
        to_unit = Select(self.driver.find_element_by_id("to-unit"))
        value_input = self.driver.find_element_by_id("value")
        result = self.driver.find_element_by_id("result")

        ## Select "Fahrenheit" as the "From" unit
        from_unit.select_by_value("Fahrenheit")

        ## Select "Celsius" as the "To" unit
        to_unit.select_by_value("Celsius")

        ## Enter a value (e.g., "86")
        value_input.clear()
        value_input.send_keys("86")
        self.driver.implicitly_wait(2)
        conversion_result = result.get_attribute("innerText")

        ## Check the conversion result
        self.assertEqual(conversion_result, "30.0", "Fahrenheit to Celsius conversion is incorrect")

    

   def test_celsius_to_kelvin_conversion(self):
        from_unit = Select(self.driver.find_element_by_id("from-unit"))
        to_unit = Select(self.driver.find_element_by_id("to-unit"))
        value_input = self.driver.find_element_by_id("value")
        result = self.driver.find_element_by_id("result")

        ## Select "Celsius" as the "From" unit
        from_unit.select_by_value("celsius")

        ## Select "Kelvin" as the "To" unit
        to_unit.select_by_value("kelvin")

        ## Enter a value (e.g., "30")
        value_input.clear()
        value_input.send_keys("30")
        self.driver.implicitly_wait(1)
        conversion_result = result.get_attribute("innerText")
        self.assertEqual(conversion_result, "303.15", "Celsius to Kelvin conversion is incorrect")


    def test_kelvin_to_celsius_conversion(self):
        from_unit = Select(self.driver.find_element_by_id("from-unit"))
        to_unit = Select(self.driver.find_element_by_id("to-unit"))
        value_input = self.driver.find_element_by_id("value")
        result = self.driver.find_element_by_id("result")

        ## Select "Kelvin" as the "From" unit
        from_unit.select_by_value("kelvin")

        ## Select "Celsius" as the "To" unit
        to_unit.select_by_value("celsius")

        ## Enter a value (e.g., "303.15")
        value_input.clear()
        value_input.send_keys("303.15")
        self.driver.implicitly_wait(1)
        conversion_result = result.get_attribute("innerText")
        self.assertEqual(conversion_result, "30.0", "Kelvin to Celsius conversion is incorrect")


 def test_fahrenheit_to_kelvin_conversion(self):
        from_unit = Select(self.driver.find_element_by_id("from-unit"))
        to_unit = Select(self.driver.find_element_by_id("to-unit"))
        value_input = self.driver.find_element_by_id("value")
        result = self.driver.find_element_by_id("result")
         ## Select "Fahrenheit" as the "From" unit
        from_unit.select_by_value("fahrenheit")

        ## Select "Kelvin" as the "To" unit
        to_unit.select_by_value("kelvin")

        ## Enter a value (e.g., "86")
        value_input.clear()
        value_input.send_keys("86")
        self.driver.implicitly_wait(2)
        conversion_result = result.get_attribute("innerText")
        self.assertEqual(conversion_result, "302.039", "Fahrenheit to Kelvin conversion is incorrect")

    def test_kelvin_to_fahrenheit_conversion(self):
        from_unit = Select(self.driver.find_element_by_id("from-unit"))
        to_unit = Select(self.driver.find_element_by_id("to-unit"))
        value_input = self.driver.find_element_by_id("value")
        result = self.driver.find_element_by_id("result")

        ## Select "Kelvin" as the "From" unit
        from_unit.select_by_value("kelvin")

        ## Select "Fahrenheit" as the "To" unit
        to_unit.select_by_value("fahrenheit")

        ## Enter a value (e.g., "302.039")
        value_input.clear()
        value_input.send_keys("302.039")
        self.driver.implicitly_wait(1)
        conversion_result = result.get_attribute("innerText")
        self.assertEqual(conversion_result, "86", "Kelvin to Fahrenheit conversion is incorrect")


    def tearDown(Input):
        Input.driver.quit()

if __name__ == "__main__":
    unittest.main()

This script includes test cases for various temperature conversions, covering Celsius to Fahrenheit, Fahrenheit to Celsius, Celsius to Kelvin, Kelvin to Celsius, Fahrenheit to Kelvin, and Kelvin to Fahrenheit conversions.
