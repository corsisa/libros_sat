# -*- coding: utf-8 -*-
{
    'name': "Libros SAT",

    'summary': """
        Libros de Venta y Compra Guatemala""",

    'description': """
        Libros de ventas y compras adaptados para una oficina contable donde se requiera
        registrar la informacion de las facturas de manera manual en los libros de venta
        y/o compras
    """,

    'author': "CORSISA, Endy Ocando",
    'website': "http://www.corsisasolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Localization',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views_compras.xml',
        'views/views_ventas.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}