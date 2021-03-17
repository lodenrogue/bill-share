from item import Item

class BillShare():

	def __init__(self):
		self.items = []


	def add_item(self, name, cost):
		self.items.append(Item(name, cost))


	def total(self):
		return sum(item.cost for item in self.items)


	def calculate_share(self, share_percent):
		return self.total() * share_percent