import unittest
from unittest.mock import MagicMock

def btn_click(numbers, text_input):
    # Update the input text with the clicked number
    operator = text_input.get()
    operator = operator + str(numbers)
    text_input.set(operator)

def btn_clear(text_input):
    # Clear the input text
    text_input.set("")

def btn_equals(text_input):
    # Evaluate the expression and update the input text with the result
    operator = text_input.get()
    try:
        sum_up = str(eval(operator))
        text_input.set(sum_up)
    except Exception as e:
        # Handle errors gracefully
        print("Error:", e)

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.text_Input = MagicMock()

    def test_btn_click(self):
        # Trigger btn_click with input '7'
        btn_click(7, self.text_Input)
        
        # Assert that the set method was called with '7' appended to the current input text
        self.text_Input.set.assert_called_once_with(self.text_Input.get() + "7")

    def test_btn_clear(self):
        # Trigger btn_clear
        btn_clear(self.text_Input)
        
        # Assert that the set method was called with an empty string
        self.text_Input.set.assert_called_once_with("")

    def test_btn_equals(self):
        # Mock the return value of the get method to simulate input '3+5'
        self.text_Input.get.return_value = "3+5"
        
        # Trigger btn_equals
        btn_equals(self.text_Input)
        
        # Assert that the set method was called with the result of '3+5', which is '8'
        self.text_Input.set.assert_called_once_with("8")

if __name__ == '__main__':
    unittest.main()
