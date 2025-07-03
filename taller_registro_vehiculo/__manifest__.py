{
    'name': 'Taller Registro Vehiculo',
    'version' : '1.0',
    'summary' : 'Registro de vehiculos por cliente para talleres',
    'category' : 'Taller',
    'author' : 'Burnet Mauricio Nicolas',
    'depends' : ['base','contacts'],
    'data' : [
        'views/taller_vehiculo_views.xml', 
        'views/taller_menu.xml',
        'security/ir.model.access.csv',
        'views/taller_visita_views.xml',
        'report/taller_visita_report.xml',
        'report/taller_visita_template.xml',
        ],
    'installable' : True,
    'application' : True,
}