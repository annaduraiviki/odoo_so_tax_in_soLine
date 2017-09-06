# -*- coding: utf-8 -*-
# (c) 2017 Vignesh
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': "Subtotal with tax in SO",

    'summary': """
       Subtotal with TAX""",

    'description': """
        This module calculates TAX amount for each SO line and display it in SO Line.
    """,
    'author': "Vignesh",
    'website': "viki2.odoo.com",
    'category': 'sale',
    'version': '10.0.0.1.0',
    'depends': ['base','sale',
                ],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': False,
    'data': [
        'views/sale_order_view.xml',
    ],
    'demo': [
    ],
}
