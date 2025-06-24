{
    'name': 'Taller Registro Vehiculo',
    'version' : '1.0',
    'summary' : 'Registro de vehiculos por cliente para talleres',
    'category' : 'Taller',
    'author' : 'Burnet Mauricio Nicolas',
    'depends' : ['base','contacts'],
    'data' : [
        'security/ir.model.access.csv',
        'views/menuitem.xml',
        'views/repuesto_views.xml',
        'views/vehiculo_views.xml',
        'templates/portal_repuesto_templates.xml',
        'templates/portal_inyectores_template.xml',
        ],
    'installable' : True,
    'applications' : True,
}