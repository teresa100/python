
robot_price = 900
robot_amount = 2
robot_tax = 1.25

book_price = 100
book_tax = 1.06
print (robot_price * robot_amount * robot_tax + book_price * book_tax)

robot = {"price": 900, "amount": 2, "tax": 1.25}
book = {"price": 100, "amount": 1, "tax": 1.06}
print(robot["price"] * robot["amount"] * robot["tax"] + book["price"] * book["amount"] * book["tax"])

class Product: 
	price = 0
	amount = 0
	tax = 1

robot = Product()
robot.price = 900
robot.amount = 2
robot.tax = 1.25

book = Product()
book.price = 100
book.amount = 1
book.tax = 1.06

print(robot.__dict__)

print(robot.price * robot.amount * robot.tax + book.price * book.amount * book.tax)


class Product:
	price = 0
	amount = 0
	tax = 1

	def price_with_tax(self):
		return self.price * self.amount * self.tax 

robot = Product()
robot.price = 900
robot.amount = 2
robot.tax = 1.25

book = Product()
book.price = 100
book.amount = 1
book.tax = 1.06


print(robot.price_with_tax() + (book.price_with_tax()))

class Product:
	def __init__(self, price, amount, tax):
		self.price = price
		self.amount = amount
		self.tax = tax

	def price_with_tax(self):
		return self.price * self.amount * self.tax 

robot = Product(price=900, amount=2, tax=1.25)
book = Product(price=100, amount=1, tax=1.06)

print(robot.price_with_tax() + book.price_with_tax())


class Product:
	def __init__(self, price, amount, tax):
		self.price = price
		self.amount = amount
		self.tax = tax

	def price_with_tax(self):
		return self.price * self.amount * self.tax 


products = [Product(price=900, amount=2, tax=1.25), Product(price=100, amount=1, tax=1.06)]
total_price = products[0].price_with_tax() + products[1].price_with_tax()
print(total_price)

products = [Product(price=900, amount=2, tax=1.25), Product(price=100, amount=1, tax=1.06)]
total_price = 0
for product in products: 
	total_price = total_price + product.price_with_tax()
print(total_price)


class Product:
	def __init__(self, price, amount, tax):
		self.price = price
		self.amount = amount
		self.tax = tax

	def price_with_tax(self):
		return self.price * self.amount * self.tax 

products = [Product(price=900, amount=2, tax=1.25), Product(price=100, amount=1, tax=1.06)]
total_price = 0
for product in products: 
	total_price = total_price + product.price_with_tax()

if total_price > 500:
	print(total_price * 0.9)

class Product:
	def __init__(self, name, price, amount, tax):
		self.name = name
		self.price = price
		self.amount = amount
		self.tax = tax

	def price_with_tax(self):
		total = self.price * self.amount * self.tax 
		if total > 500:
			return 0.9 * total
		else:
			return total 

products = [Product(name="Robot", price=900, amount=2, tax=1.25), Product(name="Book", price=100, amount=1, tax=1.06), Product(name="batteries", price=300, amount=1, tax=1.25)]
total_price = 0
for product in products: 
	total_price = total_price + product.price_with_tax()
print(total_price)

for product in products:
	print(product.name, product.price_with_tax())





