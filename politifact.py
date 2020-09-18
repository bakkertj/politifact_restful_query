#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright (C) 2020 Trevor Bakker 

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
import requests
import argparse

API_ENDPOINT = 'https://www.politifact.com/api/factchecks/'

parser = argparse.ArgumentParser( )
parser.add_argument('-slug',  help ='slug name of the politifact entry' )

args = parser.parse_args( )

params = {
    "speaker_slug" : args.slug 
}

r=requests.get(API_ENDPOINT, params = params )

print(r.json())
