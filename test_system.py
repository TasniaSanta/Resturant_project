import unittest
from system import add, CostofDrinks

class TestSystem(unittest.TestCase):

    def test_add(self):
        # Test case 1: Adding two positive numbers
        result = add(3, 5)
        self.assertEqual(result, 8)

        # Test case 2: Adding a positive and a negative number
        result = add(-3, 5)
        self.assertEqual(result, 2)

        # Test case 3: Adding two negative numbers
        result = add(-3, -5)
        self.assertEqual(result, -8)

    def test_cost_of_drinks(self):
        # Test case 1: Creating an instance of CostofDrinks
        drinks = CostofDrinks()
        self.assertIsInstance(drinks, CostofDrinks)

        # Test case 2: Checking if the default drink prices are correct
        self.assertEqual(drinks.latta, 1.2)
        self.assertEqual(drinks.espresso, 1.5)
        self.assertEqual(drinks.iced_latta, 1.8)
        self.assertEqual(drinks.vale_coffee, 2.0)
        self.assertEqual(drinks.cappuccino, 1.8)
        self.assertEqual(drinks.african_coffee, 2.0)
        self.assertEqual(drinks.american_coffee, 1.8)

if __name__ == '__main__':
    unittest.main()
