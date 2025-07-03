# -*- coding: utf-8 -*-
{
    'name': "Create Backorder Button",

    'summary': """
        Button to create delivery order a backorder""",

    'description': """
        Add a button to delivery order that changes order to backorder if one operations line
    """,

    'author': "busii",
    'website': "http://www.busii.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '18.0.1.0.0',
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': True,

    # any module necessary for this one to work correctly
    'depends': ['stock'],

    # always loaded
    'data': [
        'views/add_button.xml',
    ],
    'images': ['static/description/icon.png'],
}
