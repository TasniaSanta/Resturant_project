# Resturant_project

Classes:

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
Attributes: Order ID, order cost, date time order placed
Restaurant: Represents the restaurant itself.
Attributes: ID, name, address

Relationships:

A Customer can make one or multiple Payments.
An Owner can manage a Restaurant.
A Restaurant has Menus.
An Employee can place one or more Orders.
An Order is placed by one Customer and is associated with the Restaurant.

Usage

The Customer class is used to represent the customers of the restaurant. Customers can make Payments to the restaurant.
The Owner class is used to represent the owner of the restaurant. The Owner is responsible for managing the Restaurant.
The Menu class is used to represent the menu of the restaurant. The Menu contains all the Food items available for customers to order.
The Employee class is used to represent the employees of the restaurant.
The Order class is used to represent the orders that Customers place. An Order is associated with one Customer and one Restaurant.
The Restaurant class is used to represent the restaurant itself. The Restaurant has a Menu, a list of Employees, and a list of Orders.
