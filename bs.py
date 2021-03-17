import sys
from bill_share import BillShare

from rich.console import Console
from rich.table import Table


def run(item_file, payer1_share_percent):
	items = get_items(item_file)
	bill_share = create_bill_share(items)
	display(bill_share, payer1_share_percent)


def display(bill_share, payer1_share_percent):
	item_table = create_item_table(bill_share)
	share_table = create_share_table(bill_share, payer1_share_percent)

	console = Console()
	console.print(item_table)
	console.print(share_table)


def create_share_table(bill_share, payer1_share_percent):
	percent = float(payer1_share_percent)
	payer1_share = bill_share.calculate_share(percent)
	payer2_share = bill_share.total() - payer1_share

	table = Table(title='Pay', show_lines=True)
	table.add_column('Name', style='cyan', no_wrap=True, width=17)
	table.add_column('Amount', justify='right', no_wrap=True, width=10)

	table.add_row('Ambrin', '{:.2f}'.format(payer1_share))
	table.add_row('Miguel', '{:.2f}'.format(payer2_share))
	return table


def create_item_table(bill_share):
	table = Table(title='Items', show_lines=True)
	table.add_column('Name', style='cyan', no_wrap=True, width=17)
	table.add_column('Cost', justify='right', no_wrap=True, width=10)

	for item in bill_share.items:
		name = item.name
		cost = '{:.2f}'.format(item.cost)
		table.add_row(name, cost)

	total = '{:.2f}'.format(bill_share.total())
	table.add_row('Total', total)
	return table


def create_bill_share(items):
	bill_share = BillShare()

	for item in items:
		name = get_name(item)
		cost = get_cost(item)
		bill_share.add_item(name, cost)

	return bill_share


def get_name(item):
	return item.split(',')[0]


def get_cost(item):
	return float(item.split(',')[1].replace('\n', ''))


def get_items(file):
	with open(file, 'r') as f:
		return f.readlines()


if __name__ == '__main__':
	item_file = sys.argv[1]
	bill_share = sys.argv[2]
	run(item_file, bill_share)