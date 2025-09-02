# -*- coding: utf-8 -*-
{
    'name': "Remito X Personalizado (RolyMotors)",
    'summary': "Crea un formato de Remito X personalizado desde las entregas de inventario.",
    'description': """
        Este módulo agrega una nueva opción de impresión en los albaranes (transferencias de stock)
        para generar un PDF con un formato de Remito X no fiscal y personalizado.
    """,
    'author': "Gemini Assistant for RolyMotors",
    'category': 'Inventory/Reporting',
    'version': '17.0.1.0',
    'depends': ['stock'],  # Depende solo de inventario, no de l10n_ar
    'data': [
        'views/report_remito.xml',
        'views/sale_report_inherit.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}