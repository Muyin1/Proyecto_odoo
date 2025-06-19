{
    'name': 'Repuestos Stock',
    'version': '1.0',
    'depends': ['base', 'product', 'stock'],  
    'author': 'Burnet Mauricio Nicolas',
    'category': 'Inventory',
    'description': 'Gestión de repuestos para taller',
    'data': [
        'security/ir.model.access.csv',
        'views/repuesto_views.xml',
        'views/vehiculo_views.xml',
        'views/inyector_views.xml',
        'templates/repuesto_portal_templates.xml',
    ],
    'installable': True,
    'application': True,
}
