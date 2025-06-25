{
    'name': 'Repuestos Stock',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Gestión personalizada de repuestos para taller y ventas',
    'author': 'Nicolás',
    'depends': ['product', 'website'],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/repuesto_views.xml',
        'views/vehiculo_views.xml',
        'views/menuitem.xml',
        'templates/portal_repuesto_templates.xml',
        'templates/portal_inyector_template.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'repuestos_stock/static/src/js/repuesto_form.js',
        ],
    },
}