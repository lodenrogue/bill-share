import sys
import argparse
from bill_share import BillShare

from rich.console import Console

from table.html_table import HtmlTable
from table.rich_table import RichTable

def run(item_file, payer1_share_percent, is_html):
    items = get_items(item_file)
    bill_share = create_bill_share(items)

    payer1_amount = bill_share.calculate_share(float(payer1_share_percent))
    payer2_amount = bill_share.total() - payer1_amount

    payer1 = create_payer("Ambrin", payer1_amount)
    payer2 = create_payer("Miguel", payer2_amount)

    if is_html:
        display_html_table(bill_share, payer1, payer2)
    else:
        display_rich_table(bill_share, payer1, payer2)


def create_payer(name, amount):
    return {
        "name": name,
        "amount": amount
    }


def display_html_table(bill_share, payer1, payer2):
    table = HtmlTable(bill_share, payer1, payer2)
    items = table.create_item_table()
    share = table.create_share_table()

    print("Items")
    print("<br/>")
    print(items)
    print("<br/><br/>")

    print("Pay")
    print("<br/>")
    print(share)


def display_rich_table(bill_share, payer1, payer2):
    table = RichTable(bill_share, payer1, payer2)
    items = table.create_item_table()
    share = table.create_share_table()

    console = Console()
    console.print(items)
    console.print(share)


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


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("item_file", help="file containing items")
    parser.add_argument("share", help="payer 1 share percentage")
    parser.add_argument("-l", "--html", help="print tables in html", action="store_true")
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    run(args.item_file, args.share, args.html)
