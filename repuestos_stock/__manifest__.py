{
    'name': 'Repuestos Stock',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Burnet Mauricio Nicolas',
    'category': 'Inventory',
    'description': 'Gestión de repuestos para taller',
    'data': [
        'views/marca_views.xml',
        'views/repuesto_menu_views.xml',
        'security/ir.model.access.csv',
        'views/vehiculo_views.xml',
        'views/repuesto_views.xml',
    ],
    'installable': True,
    'application': True,
}
