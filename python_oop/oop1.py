import csv

class Item:
    # Class attribute
    pay_rate = 0.8 # The pay rate after 20% discout

    all = []

    # Instance attribute
    # constructor __init__ for instance
    def __init__(self, name: str, price: float, quantity=0):
        # Statement keyword
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0

        if isinstance(num, float):
            # Count out hte floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f'Item("{self.name}", {self.price}, {self.quantity})'
    

print(Item.is_integer(7.0))
Item.instantiate_from_csv()
print(Item.all)
