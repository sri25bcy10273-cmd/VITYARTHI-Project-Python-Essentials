# Pharmacy Stock CRUD System
class PharmacyStock:
    def __init__(self):
        self.stock = {}

    def create_medicine(self, name, quantity, price):
        if name in self.stock:
            return f"Medicine '{name}' already exists."
        self.stock[name] = {'quantity': quantity, 'price': price}
        return f"Medicine '{name}' added successfully."

    def read_medicine(self, name):
        if name not in self.stock:
            return f"Medicine '{name}' not found."
        return self.stock[name]

    def update_medicine(self, name, quantity=None, price=None):
        if name not in self.stock:
            return f"Medicine '{name}' not found."
        if quantity is not None:
            self.stock[name]['quantity'] = quantity
        if price is not None:
            self.stock[name]['price'] = price
        return f"Medicine '{name}' updated successfully."

    def delete_medicine(self, name):
        if name not in self.stock:
            return f"Medicine '{name}' not found."
        del self.stock[name]
        return f"Medicine '{name}' deleted successfully."
# Example usage
pharmacy = PharmacyStock()
print(pharmacy.create_medicine("Aspirin", 100, 5.99))
print(pharmacy.read_medicine("Aspirin"))
print(pharmacy.update_medicine("Aspirin", quantity=150))
print(pharmacy.delete_medicine("Aspirin"))
