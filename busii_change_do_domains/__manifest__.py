# -*- coding: utf-8 -*-
{
    'name': "Remove Backorders from Non Backorder Picking Type",

    'summary': """
        Removes Backorders from Picking Type""",

    'description': """
        Will remove backorders from the picking type domains that are not backorders. 
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
    # 'data': [
    # ],
    'images': ['static/description/icon.png'],
}
