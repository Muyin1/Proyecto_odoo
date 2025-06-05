from odoo import models, fields

class Vehiculo(models.Model):
    _name = 'taller.vehiculo'
    _description = 'Vehiculo del Cliente'

    vehiculo_id = fields.Many2one('taller.vehiculo', string='Vehiculo', required=True)
    fecha = fields.Date(string='Fecha de la Visita', required=True)
    tipo_trabajo = fields.Selection([
        ('escaneo', 'Escaneo'),
        ('service', 'Service'),
        ('cambio_distribucion', 'Cambio de Distribucion'),
        ('otro', 'Otro'),
    ], string='Tipo de Trabajo', required=True)
    notras = fields.Text(string='Notas')
    piezas_usadas = fields.One2many('taller.visita.pieza', 'visita_id', string='Piezas Utilizadas')

