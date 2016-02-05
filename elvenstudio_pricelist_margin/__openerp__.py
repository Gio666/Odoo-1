# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: ElvenStudio
#    Copyright 2015 elvenstudio.it
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
 'name': 'Product Pricelist Margin',
 'license': 'AGPL-3',
 'version': '0.1.0',
 'category': 'Sales & Purchases',
 'website': 'https://github.com/ElvenStudio/Odoo',
 'summary': "Calculate margin and margin rates from pricelist",
 'description': """
Extend Pricelist with margin calculation
==============================================================

This module extend the module product_pricelist adding the capability of calculate
the product margin for a pricelist and the margin rate.

TODO
----
 - Display margin rate as percentage

    """,
 'author': "ElvenStudio",
 'license': 'AGPL-3',
 'website': 'http://www.elvenstudio.it',

 'images': ['images/elvenstudio.png', ],

 'depends': [
     'product',
     'product_pricelist',
 ],

 'data': [
     'views/product_view.xml',
 ],

 'installable': True,
 'application': False,
 }
