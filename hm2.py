'''class Product:
    def init(self, name, price, quantity):
        self.name = name         # Назва товару
        self.price = price          # Ціна за одиницю
        self.quantity = quantity    # Кількість одиниць

    def calculate_all_price(self):
        return self.price * self.quantity

    def display_info(self):
        print(f"Товар: {self.name}")
        print(f"Ціна за одиницю: {self.price} грн")
        print(f"Кількість: {self.quantity}")
        print(f"Загальна вартість: {self.calculate_all_price()} грн")
        print("-" * 30)
price = {"Яблуко": {"price": 10, "quantity": 5},
    "Банан": {"price": 15, "quantity": 3},
    "Помідор": {"price": 12, "quantity": 4},
    "Огірок": {"price": 8, "quantity": 6},
    "Гранат": {"price": 25, "quantity": 2},
    "Апельсин": {"price": 18, "quantity": 5},
    "Ківі": {"price": 20, "quantity": 4},
    "Петрушка": {"price": 9, "quantity": 7}}

# Виведення інформації про кожен товар
total_price = 0
for product in price:
    product.display_info()
    total_sum += product.calculate_total_price()

print(f"Загальна сума за всі товари: {total_price} грн") '''
'''class Car'''
