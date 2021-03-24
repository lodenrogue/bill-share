from prettytable import PrettyTable

class HtmlTable():

    def __init__(self, bill_share, payer1, payer2):
        self.bill_share = bill_share
        self.payer1 = payer1
        self.payer2 = payer2

    
    def create_item_table(self):
        table = PrettyTable()
        table.field_names = ["Name", "Cost"]
        
        table.align["Name"] = "l"
        table.align["Cost"] = "r"

        for item in self.bill_share.items:
            name = item.name
            cost = '{:.2f}'.format(item.cost)

            table.add_row([name, cost])

        total = '{:.2f}'.format(self.bill_share.total())
        table.add_row(["Total", total])
        return table.get_html_string()


    def create_share_table(self):
        table = PrettyTable()
        table.field_names = ["Name", "Amount"]

        table.align["Name"] = "l"
        table.align["Amount"] = "r"

        payer1_amount = '{:.2f}'.format(self.payer1["amount"])
        payer2_amount = '{:.2f}'.format(self.payer2["amount"])

        table.add_row([self.payer1["name"], payer1_amount])
        table.add_row([self.payer2["name"], payer2_amount])

        return table.get_html_string()      
