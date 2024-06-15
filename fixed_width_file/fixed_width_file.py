import logging

logger = logging.getLogger(__name__)


class FixedWidthFile:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.header = None
        self.transactions = []
        self.footer = None
        self.load_file()

    def load_file(self):
        with open(self.filepath, 'r') as file:
            lines = file.readlines()
            self.header = self.parse_header(lines[0])
            self.footer = self.parse_footer(lines[-1])
            self.transactions = [self.parse_transaction(line) for line in lines[1:-1]]

    def parse_header(self, line: str):
        return {
            "field_id": line[0:2].strip(),
            "name": line[2:30].strip(),
            "surname": line[30:60].strip(),
            "patronymic": line[60:90].strip(),
            "address": line[90:120].strip()
        }

    def parse_transaction(self, line: str):
        return {
            "field_id": line[0:2].strip(),
            "counter": line[2:8].strip(),
            "amount": line[8:20].strip(),
            "currency": line[20:23].strip(),
            "reserved": line[23:120].strip()
        }

    def parse_footer(self, line: str):
        return {
            "field_id": line[0:2].strip(),
            "total_counter": line[2:8].strip(),
            "control_sum": line[8:20].strip(),
            "reserved": line[20:120].strip()
        }

    def get_field(self, section: str, field: str):
        if section == "header":
            return self.header[field]
        elif section == "footer":
            return self.footer[field]
        elif section.startswith("transaction"):
            index = int(section.split("_")[1])
            return self.transactions[index][field]

    def set_field(self, section: str, field: str, value: str):
        if section == "header":
            self.header[field] = value
        elif section == "footer":
            self.footer[field] = value
        elif section.startswith("transaction"):
            index = int(section.split("_")[1])
            self.transactions[index][field] = value

    def add_transaction(self, amount: str, currency: str):
        counter = str(len(self.transactions) + 1).zfill(6)
        transaction = {
            "field_id": "02",
            "counter": counter,
            "amount": amount.zfill(12),
            "currency": currency,
            "reserved": ""
        }
        self.transactions.append(transaction)
        self.update_footer()

    def update_footer(self):
        total_counter = str(len(self.transactions)).zfill(6)
        control_sum = sum(int(t["amount"]) for t in self.transactions)
        self.footer["total_counter"] = total_counter
        self.footer["control_sum"] = str(control_sum).zfill(12)

    def save_file(self):
        with open(self.filepath, 'w') as file:
            file.write(self.format_header() + "\n")
            for transaction in self.transactions:
                file.write(self.format_transaction(transaction) + "\n")
            file.write(self.format_footer() + "\n")

    def format_header(self):
        return f"{self.header['field_id']: <2}{self.header['name']: <28}{self.header['surname']: <30}{self.header['patronymic']: <30}{self.header['address']: <30}"

    def format_transaction(self, transaction):
        return f"{transaction['field_id']: <2}{transaction['counter']: <6}{transaction['amount']: <12}{transaction['currency']: <3}{transaction['reserved']: <97}"

    def format_footer(self):
        return f"{self.footer['field_id']: <2}{self.footer['total_counter']: <6}{self.footer['control_sum']: <12}{self.footer['reserved']: <100}"
