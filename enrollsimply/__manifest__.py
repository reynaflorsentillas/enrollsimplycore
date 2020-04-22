# -*- coding: utf-8 -*-
{
    'name': "enrollsimply",

    'summary': """
        EnrollSimply Branding and Base Modules""",

    'description': """
        - EnrollSimply Branding
        - Related Modules: EnrollSimply Provider
    """,

    'author': "Omnitechnical",
    'website': "http://www.omnitechnical.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','app_odoo_customize','mail_bot','enrollsimply_provider'],
    #'depends': ['base','app_odoo_customize','mail_bot'],

    # always loaded
    'data': [
        'data/res_partner_data.xml',
        'views/assets.xml',
    ],    
    'installable': True,
    'application': True,
    'auto_install': True,
}
