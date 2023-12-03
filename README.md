# Resturant_project

Classes

Customer: Represents a customer of the restaurant.
Attributes: Name, phone number, age, address
Payment: Represents a payment made by a customer.
Attributes: Card number, card type, amount
Owner: Represents the owner of the restaurant.
Attributes: Name, phone number, age, address
Menu: Represents the menu of the restaurant.
Attributes: Food item name, price, availability
Employee: Represents an employee of the restaurant.
Attributes: Name, phone number, age, address
Order: Represents an order placed by a customer.
Attributes: Order ID, order cost, datetime order placed
Restaurant: Represents the restaurant itself.
Attributes: ID, name, address

Relationships
A Customer can make multiple Payments.
An Owner can manage one Restaurant.
A Restaurant has one Menu.
An Employee can place one or more Orders.
An Order is placed by one Customer and is associated with one Restaurant.

