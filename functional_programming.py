#Final Data Structures:

# Define drinks and dictionary
drinks_dict = {
    "coffee": 2.5,
    "tea": 2.0,
    "juice": 3.0
}
cakes_dict = {
    "chocolate": 4.0,
    "vanilla": 3.5,
    "strawberry": 3.8
}
#Side-effect-free Functions:
def calculate_costs(drinks, cakes):
    """Calculate total costs of drinks and cakes."""
    total_drinks_cost = sum(drinks.values())
    total_cakes_cost = sum(cakes.values())
    return total_drinks_cost + total_cakes_cost

# Functions as Parameters and Return Values:
def apply_discount(discount_rate):
    #Returns a function to apply discount to the total cost.
    #Closures / Anonymous Functions:
    def discount(total_cost):
        #Apply discount to the total cost.
        return total_cost * (1 - discount_rate)
    return discount

# Example usage:
total_cost = calculate_costs(drinks_dict, cakes_dict)
print("Total cost before discount:", total_cost)

# Apply a 10% discount using a higher-order function
discount_function = apply_discount(0.1)
discounted_cost = discount_function(total_cost)
print("Total cost after 10% discount:", discounted_cost)
