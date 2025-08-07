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
        'views/taller_visita_views.xml',
        'security/ir.model.access.csv',
        'report/taller_report.xml',

        ],
    'installable' : True,
    'application' : True,
}