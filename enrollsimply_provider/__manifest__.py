# -*- coding: utf-8 -*-
{
    'name': "enrollsimply_provider",

    'summary': """
        EnrollSimply Provider Information""",

    'description': """
        - EnrollSimply Provider Information
    """,

    'author': "Omnitechnical",
    'website': "http://www.omnitechnical.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/res_partner_data.xml',
        'views/assets.xml',
    ],    
    'installable': True,
    'application': True,
    'auto_install': True,
}
