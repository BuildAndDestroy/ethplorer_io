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
import types

import prettytable

from ethplorer_api import *


def filter_api_call(api_call):
    """Sort api call into three lists."""
    value_isformat_ready = []
    value_is_dictionary = []
    value_is_list = []
    for key, value in api_call.iteritems():
        if isinstance(value, (types.StringTypes, types.IntType, types.FloatType)):
            temp_dict = {}
            temp_dict[key] = value
            value_isformat_ready.append(temp_dict)
        elif isinstance(value, types.DictionaryType):
            temp_dict = {}
            temp_dict[key] = value
            value_is_dictionary.append(temp_dict)
        elif isinstance(value, types.ListType):
            temp_dict = {}
            temp_dict[key] = value
            value_is_list.append(temp_dict)
    combined_lists = [value_isformat_ready, value_is_dictionary, value_is_list]
    if not value_isformat_ready:
        value_isformat_ready.append('No data found!')
    if not value_is_dictionary:
        value_is_dictionary.append('No dictionaries found!')
    if not value_is_list:
        value_is_list.append('No lists found!')
    return combined_lists


def bypass_tokens_key(third_list_of_dictionaries):
    token_for_decoration = []
    tokenInfo_list = []
    if third_list_of_dictionaries == 'No lists found!':
        return ['No list to decorate!', 'TokenInfo does not exist!']
    for keys, values in third_list_of_dictionaries.iteritems():
        for lists in values:
            for keys, values in lists.iteritems():
                if isinstance(values, types.DictionaryType):
                    tokenInfo_list.append(values)
                    for key, value in values.iteritems():
                        if key == 'name':
                            token_for_decoration.append((u'tokenInfo', value))
                token_for_decoration.append((keys, values))
    lists_for_decoration = [list(lists) for lists in token_for_decoration]
    lists_for_decoration = [
        lists for lists in lists_for_decoration if not isinstance(lists[1], types.DictType)]
    combined_lists = [lists_for_decoration, tokenInfo_list]
    return combined_lists


def token_info_details(tokens_key_value):
    """Separate tokenInfo details and pricing dictionaries."""
    token_info_details = []
    token_pricing = []
    if tokens_key_value == 'TokenInfo does not exist!':
        return ['TokenInfo details do not exist!', 'Token pricing does not exist!']
    for dictionary in tokens_key_value:
        for key, value in dictionary.iteritems():
            if isinstance(value, types.DictionaryType):
                temp_dict = {}
                temp_dict[key] = value
                token_pricing.append([[dictionary['name']], temp_dict])
        dictionary = {key: value for key,
                      value in dictionary.items() if key != 'price'}
        token_info_details.append(dictionary)
    return [token_info_details, token_pricing]


def decorate_key_value(address_and_counttxs):
    """Table format for countTxs."""
    for dicts in address_and_counttxs:
        for keys, values in dicts.iteritems():
            table = prettytable.PrettyTable([keys])
            table.add_row([values])
        table.align = 'l'
        print table


def decorate_dictionary_list(dictionary_list):
    """Table for Ethereum data."""
    for key, value in dictionary_list[0].iteritems():
        table = prettytable.PrettyTable([key])
        for keys, values in value.iteritems():
            table.add_row(['{}: {}'.format(keys, values)])
    table.align = 'l'
    print table


def decorate_tokens_key_value(tokens_key_value):
    """Table format for tokens data."""
    if tokens_key_value == 'No list to decorate!':
        return
    headers = [lists for lists in tokens_key_value[3::4]]
    token_attributes = []
    for lists in tokens_key_value:
        if lists[0] != 'tokenInfo':
            token_attributes.append(lists)
    token_attributes = [lists for lists in token_attributes]
    rows = [token_attributes[x:x + 3]
            for x in range(0, len(token_attributes), 3)]
    for header_lists, content_lists in zip(headers, rows):
        table = prettytable.PrettyTable(
            ['{}: {}'.format(header_lists[0], header_lists[1])])
        for index in content_lists:
            table.add_row(['{}: {}'.format(index[0], index[1])])
        table.align = 'l'
        print table


def decorate_token_details(token_details):
    """Table format token details, pricing separated to decorate_token_pricing."""
    if token_details == 'TokenInfo details do not exist!':
        return
    for dictionary in token_details:
        table = prettytable.PrettyTable([dictionary['name']])
        for key, value in dictionary.iteritems():
            if key != 'name':
                table.add_row(['{}: {}'.format(key, value)])
        table.align = 'l'
        print table


def decorate_token_pricing(token_details):
    """Format pricing of tokens to a table."""
    if token_details == 'Token pricing does not exist!':
        return
    for lists in token_details:
        table = prettytable.PrettyTable(['Pricing: {}'.format(lists[0][0])])
        for key, value in lists[1]['price'].iteritems():
            table.add_row(['{}: {}'.format(key, value)])
        table.align = 'l'
        print table


def main():
    """For debugging, informs user the this file is for getAddressInfo."""
    return 'This file is specific to getAddressInfo parameter passed within the API call.'


if __name__ == '__main__':
    main()
