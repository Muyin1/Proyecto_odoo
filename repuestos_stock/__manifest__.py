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
        'views/assets.xml',         # para fallback si el manifest falla
        'security/ir.model.access.csv',
        'views/menuitem.xml',
        'views/repuesto_views.xml',
        'views/vehiculo_views.xml',
        'templates/portal_repuesto_templates.xml',
        'templates/portal_inyector_template.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'repuestos_stock/static/src/js/repuesto_form.js',
            'repuestos_stock/static/src/css/repuesto_form.css',
        ],
    },
    'installable': True,
    'application': True,
}
