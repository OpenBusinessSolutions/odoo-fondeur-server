# -*- coding: utf-8 -*-
{
    'name': "Check Vaucher Do",

    'summary': """
        To handle the concepts of checks.""",

    'description': """
        This module is created to manage the concepts of checks in vouchers.
    """,

    'author': "Open Business Solutions OBS",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting &amp; Finance',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account_check_writing'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}