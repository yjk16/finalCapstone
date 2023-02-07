class Shoe:
    """
    This is the Shoe class.  It has the instance variables of 'country', 'code', 'product', 'cost' and 'quantity'.
    It has the method get_cost which will print the cost of the product.
    It has the method get_quantity which will print the quantity of the product.
    It has the method change_cost which will change the stored cost of a product.
    It has the method change_quantity which will change the stored quantity of a product.
    It has the method get_code which will return the code of the product.
    And it has the repr method which will return the string version of the product (rather than the memory address).
    """

    def __init__(self, country, code, product, cost, quantity):
        """
        initialises the following instance variables...

        :param country: the country of origin of the shoe
        :param code: the SKU code of the shoe
        :param product: the product name of the shoe
        :param cost: the cost of the shoe
        :param quantity: the quantity currently in stock for the shoe
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        """
        gets cost of the shoe

        :return: the float value of the current cost of the shoe
        """
        return float(self.cost)

    def get_quantity(self):
        """
        gets the quantity of the shoe

        :return: the integer value of the quantity of shoe currently in stock
        """
        return int(self.quantity)

    def get_code(self):
        """
        gets the SKU code of the shoe

        :return: the SKU code
        """
        return self.code

    def change_cost(self, new_cost):
        """
        changes the cost of the shoe

        :param new_cost: the updated cost of the shoe

        :return: the float value of the new cost
        """
        self.cost = float(new_cost)

    def change_quantity(self, new_quantity):
        """
        changes the quantity of the shoe

        :param new_quantity: the updated quantity of the shoe

        :return: the integer value of the new quantity
        """
        self.quantity = int(new_quantity)

    # I've used __repr__ instead of __str__. Hope this is ok.
    def __repr__(self):
        """
        This is a string representation of the shoe object

        :return: A string representation of the shoe including the product name, the SKU code,
        the current cost and current quantity recorded in the inventory
        """
        return f"The {self.product} has the code: {self.code}, costs {self.cost}R " \
               f"and there are currently {self.quantity} in stock."
