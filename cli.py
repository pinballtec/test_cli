import argparse
import os
from fixed_width_file.fixed_width_file import FixedWidthFile


def main():
    parser = argparse.ArgumentParser(description="Fixed Width File CLI")
    parser.add_argument('filepath', help="Path to the fixed width file")
    subparsers = parser.add_subparsers(dest='command')

    get_parser = subparsers.add_parser('get', help="Get field value")
    get_parser.add_argument('section', help="Section (header, footer, transaction_x)")
    get_parser.add_argument('field', help="Field name")

    set_parser = subparsers.add_parser('set', help="Set field value")
    set_parser.add_argument('section', help="Section (header, footer, transaction_x)")
    set_parser.add_argument('field', help="Field name")
    set_parser.add_argument('value', help="New value")

    add_parser = subparsers.add_parser('add', help="Add transaction")
    add_parser.add_argument('amount', help="Transaction amount")
    add_parser.add_argument('currency', help="Transaction currency")

    args = parser.parse_args()

    if not os.path.exists(args.filepath):
        print(f"Error: The file {args.filepath} does not exist.")
        return

    file = FixedWidthFile(args.filepath)

    if args.command == 'get':
        value = file.get_field(args.section, args.field)
        print(f"Value of {args.field} in {args.section}: {value}")
    elif args.command == 'set':
        file.set_field(args.section, args.field, args.value)
        file.save_file()
        print(f"Updated {args.field} in {args.section}")
    elif args.command == 'add':
        file.add_transaction(args.amount, args.currency)
        file.save_file()
        print(f"Added transaction with amount {args.amount} and currency {args.currency}")


if __name__ == "__main__":
    main()
