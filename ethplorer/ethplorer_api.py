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

import json
import urllib


class EthplorerAPI(object):
    """Parsed Variables to build EthplorerAPI."""

    def __init__(self, command, address=None, limit=None, token_address=None, criteria=None, formatted=None):
        self.url = 'https://api.ethplorer.io'
        self.api_key = '?apiKey=freekey'
        self.command = command
        self.address = address or None
        self.limit = limit or None
        self.token_address = token_address or None
        self.criteria = criteria or None
        self.formatted = formatted
        self.limit_url = '{}&type=transfer&limit={}'.format(
            self.api_key, self.limit)
        self.token = '&token='
        self.token_url = '{}&token={}&type=transfer'.format(
            self.api_key, self.token_address)
        self.top_token = '/getTop{}&criteria={}'.format(
            self.api_key, self.criteria)

    def simple_api_call(self):
        """Make the API call, import as unicode, push to string format."""
        for address in self.address:
            print '{}/{}/{}{}'.format(self.url, self.command, address, self.api_key)
            response = urllib.urlopen(
                '{}/{}/{}{}'.format(self.url, self.command, address, self.api_key))
            data = json.loads(response.read())
            return data


def main():
    return 'This file is for creating the API call to api.ethplorer.io.'


if __name__ == '__main__':
    main()
