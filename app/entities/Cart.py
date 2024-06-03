class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        if product['price'] < 0:
            raise ValueError("Price cannot be negative")
        self.items.append(product)

    def remove_product(self, product_id):
        self.items = [item for item in self.items if item['id'] != product_id]

    def total(self):
        total = sum(item['price'] for item in self.items)
        for item in self.items:
            if item['price'] > 100:
                total -= item['price'] * 0.10
        return total
