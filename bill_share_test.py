import unittest
from bill_share import BillShare

class BillShareTest(unittest.TestCase):

	def test_calculate_total_cost(self):
		item1_price = 10.2
		item2_price = 245.75

		input_total = item1_price + item2_price

		share = self.create_share(item1_price, item2_price)
		result_total = share.total()

		self.assertEqual(input_total, result_total)


	def test_calculate_payer_share(self):
		item1_price = 100
		item2_price = 34.60
		total = item1_price + item2_price

		payer1_percent = .3659
		expected_share = total * payer1_percent

		share = self.create_share(item1_price, item2_price)
		result_share = share.calculate_share(payer1_percent)

		self.assertEqual(expected_share, result_share)


	def create_share(self, item1_price, item2_price):
		share = BillShare()
		share.add_item("Item1", item1_price)
		share.add_item("Item2", item2_price)
		return share


if __name__ == '__main__':
	unittest.main()