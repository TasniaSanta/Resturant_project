import unittest
from tkinter import Tk, Text
from tkinter.messagebox import askyesno
from unittest.mock import MagicMock, patch
from tkinter import DISABLED

# Import the functions to be tested
from system import (
    calculate_costs,
    check_latta,
    check_espresso,
    check_iced_latta,
    check_vale_coffee,
    check_cappucino,
    check_african_coffee,
    check_american_coffee,
    check_iced_cappucino,
    check_school_cake,
    check_sunny_ao_cake,
    check_jonathan_yo_cake,
    check_west_africa_cake,
    check_lagos_choclte_cake,
    check_kilburn_chocolate_cake,
    check_carlton_hill_cake,
    check_queen_park_cake,
)

class TestRestaurantManagementSystem(unittest.TestCase):
    def setUp(self):
        # Set up the Tkinter root and text widgets
        self.root = Tk()
        self.text = Text(self.root)
    
    def test_calculate_costs(self):
        # Test the calculate_costs function
        # You can mock the Entry widgets and StringVars to simulate user input
        E_Latta_mock = MagicMock()
        E_Latta_mock.get.return_value = "2"
        # Similarly, mock other Entry widgets and StringVars as needed
        
        # Call the function and check if the calculations are correct
        calculate_costs()
        self.assertEqual(CostofDrinks.get(), "€3.98")  # Adjust the expected value based on your calculations
        # Check other calculated values
        
    def test_check_latta(self):
        # Test the check_latta function
        # Mock the var1 variable and the txtLatta Entry widget
        var1_mock = MagicMock()
        var1_mock.get.return_value = 1
        txtLatta_mock = MagicMock()
        
        # Call the function and assert that it enables or disables the Entry widget based on the var1 value
        check_latta()
        txtLatta_mock.configure.assert_called_once_with(state=DISABLED)  # Adjust this based on your logic
    
    # Write similar test methods for other functions like check_espresso, check_iced_latta, etc.

if __name__ == "__main__":
    unittest.main()
