{
    'name': 'Repuestos Stock',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Gestión personalizada de repuestos para taller y ventas',
    'author': 'Nicolás',
    'license': 'LGPL-3',
    'depends': [
        'base',           # aunque base siempre está, ayuda a la claridad
        'web',            # FormController, FormView, view_registry…
        'product',        # hereda product.template
        'point_of_sale',  # define available_in_pos en product.template
        'website',        # si seguís usando plantillas portal
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/repuesto_views.xml',
        'views/vehiculo_views.xml',
        'views/menuitem.xml',
        'templates/portal_repuesto_templates.xml',
        'templates/portal_inyector_template.xml',
    ],
    'installable': True,
    'application': True,
}
