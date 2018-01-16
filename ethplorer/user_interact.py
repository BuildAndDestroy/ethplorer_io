#!/usr/bin/env python
"""Ethplorer API call to pull transactional data for digital currencies.

Copyright (C) 2017  Mitch O'Donnell devreap1@gmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import argparse

from get_address_info import *


def parse_arguments():
    """Collect user arguments to parse through main and build the EthplorerAPI class."""
    legal_statement = 'ethplorer_api.py Copyright (C) 2017  Mitch O\'Donnell\nThis program comes with ABSOLUTELY NO WARRANTY.\nThis is free software, and you are welcome to redistribute it\nunder certain conditions.'
    url = 'https://ethplorer.io/'
    api_documentation = 'https://github.com/EverexIO/Ethplorer/wiki/Ethplorer-API?from=etop#get-address-info'
    api_address = 'https://api.ethplorer.io/<Positional_Argument_Here>/<Address_Goes_here>?apiKey=freekey'
    epilog = '[*] Ethplorer Website: {}\r\n[*] API Documentation: {}\r\n[*] API Syntax Address: {}\r\n\r\n{}'.format(
        url, api_documentation, api_address, legal_statement)

    parser = argparse.ArgumentParser(
        description=__doc__, epilog=epilog, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-f', '--formatted', action='store_true',
                        help='Format output into tables.')

    subparsers = parser.add_subparsers(help='commands', dest='command')

    get_address_info = subparsers.add_parser(
        'getAddressInfo', help='API call for getAddressInfo.')
    get_address_info.add_argument(
        'address', nargs=1, help='Positional argument requires an address.')
    get_address_info.add_argument(
        '-t', '--token', nargs=1, help='Show balances for specified token address only.')

    get_address_history = subparsers.add_parser(
        'getAddressHistory', help='API call for getAddressHistory.')
    get_address_history.add_argument(
        'address', nargs='+', help='Show history for an address.')
    get_address_history.add_argument(
        '-o', '--token', nargs=1, help='Show only specified token address operations.')
    get_address_history.add_argument(
        '-t', '--type', nargs=1, help='Show operations of specified type only.')
    get_address_history.add_argument('-l', '--limit', action='store', type=int, choices=range(
        10), help='Add a limit from 1 to 10 last address operations.')

    get_address_transactions = subparsers.add_parser(
        'getAddressTransactions', help='API call for getAddressTransactions.')
    get_address_transactions.add_argument(
        'address', nargs=1, help='Show list of address transactions.')
    get_address_transactions.add_argument('-l', '--limit', action='store', type=int, choices=range(
        50), help='Maximum number of operations [1 - 50, default = 10]')
    # get_address_transactions.add_argument('-s', '--show', action='')

    get_token_info = subparsers.add_parser(
        'getTokenInfo', help='API call for getTokenInfo.')
    get_token_info.add_argument(
        'token', nargs=1, help='Show all Token Information for each token specified.')

    get_token_history = subparsers.add_parser(
        'getTokenHistory', help='API call for getTokenHistory.')
    get_token_history.add_argument(
        'address', nargs=1, help='Positional argument requires address(es).')
    get_token_history.add_argument(
        '-t', '--type', nargs=1, help='Show operations of specified type only.')
    get_token_history.add_argument('-l', '--limit', action='store', type=int, choices=range(
        10), help='Maximum number of operations [1 - 10, default = 10]')

    get_tx_info = subparsers.add_parser(
        'getTxInfo', help='API call for getTxInfo.')
    get_tx_info.add_argument('transaction', nargs='+',
                             help='Transaction hash(es) required.')

    get_top = subparsers.add_parser('getTop', help='API call for getTop.')
    get_top.add_argument('-c', '--criteria', action='store', choices=[
                         'trade', 'cap', 'count'], help='Sort tokens by criteria [optional, trade - by trade volume, cap - by capitalization, count - by operations, default = trade]')
    get_top.add_argument('-l', '--limit', action='store', type=int, choices=range(
        50), help='Maximum number of tokens [optional, 1 - 50, default = 50]')

    get_top_tokens = subparsers.add_parser(
        'getTopTokens', help='API call for getTopTokens.')
    get_top_tokens.add_argument('-p', '--period', action='store', type=int, choices=range(
        30), help='Show tokens for specified days period only [optional, 30 days if not set, max. is 30 days for free API key]')
    get_top_tokens.add_argument('-l' '--limit', action='store', type=int, choices=range(
        50), help='Maximum number of tokens [1 - 50, default = 50].')

    get_token_history_grouped = subparsers.add_parser(
        'getTokenHistoryGrouped', help='API call for getTokenHistoryGrouped.')
    get_token_history_grouped.add_argument(
        'address', nargs=1, help='Positional argument requires address(es).')
    get_token_history_grouped.add_argument('-p', '--period', action='store', type=int, choices=range(
        90), help='Show operations of specified days number only [optional, 30 days if not set, max. is 90 days]')

    get_token_price_history_grouped = subparsers.add_parser(
        'getTokenPriceHistoryGrouped', help='API call for getTokenPriceHistoryGrouped.')
    get_token_price_history_grouped.add_argument(
        'address', nargs=1, help='Positional argument requires address(es).')
    get_token_price_history_grouped.add_argument('-p', '--period', action='store', type=int, choices=range(
        365), help='Show price history of specified days number only [optional, 365 days if not set].')

    arguments = parser.parse_args()
    return arguments


def main():
    """Main compiles user arguments and builds the EthplorerAPI class.

    Output is json format unless -f was specified.
    """
    args = parse_arguments()

    if args.command == 'getAddressInfo' and args.formatted is False:
        ethplorer_api = EthplorerAPI(
            args.command, args.address, args.formatted, args.token)
        print ethplorer_api.simple_api_call()
    if args.command == 'getAddressInfo' and args.formatted is True:
        ethplorer_api = EthplorerAPI(
            args.command, args.address, args.formatted, args.token)
        lists_of_dictionaries = filter_api_call(
            ethplorer_api.simple_api_call())
        if lists_of_dictionaries[0][0] == 'No data found!':
            print lists_of_dictionaries[1][0]['error']
            return
        tokens_key_value = bypass_tokens_key(lists_of_dictionaries[2][0])
        token_details = token_info_details(tokens_key_value[1])

        decorate_key_value(lists_of_dictionaries[0])
        decorate_dictionary_list(lists_of_dictionaries[1])
        decorate_tokens_key_value(tokens_key_value[0])
        decorate_token_details(token_details[0])
        decorate_token_pricing(token_details[1])


if __name__ == '__main__':
    main()
