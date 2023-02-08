# finalCapstone
An OOP based system to add to, search for and update an inventory for shoes.
This is a Python program that uses OOP (Object-Oriented Programming).

The Shoe class is kept in a separate file (shoe.py) and has the parameters of 'country', 'code', 'product', 'cost' and 'quantity'.
There are getters in the Shoe class (methods to get the value) for 'code', 'cost' and 'quantity'.
There are setters in the Shoe class (methods to set or change the value) for 'cost' and 'quantity'.
Finally, there is a repr method included in the Shoe class, which returns a string representation of a shoe object when it is called.

The program inventory.py allows a user to view a list of shoes from an inventory, the details of which include
which country the shoe originates from, the SKU code, the name of the shoe, the cost of the shoe and the current quantity in stock.
The data (details) of the shoe are kept in a separate text file (inventory.txt) and are called by the code in inventory.py whenever necessary.
Other functions included in the program are the ability to check the values of the shoes; create the details of a new shoe and add them to the inventory;
to search for a shoe by its SKU code and check the current cost and quantity; restock the shoe with the lowest quantity;
and find the shoe with the highest quanitity and reduce the price of this shoe.
