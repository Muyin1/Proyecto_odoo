from odoo import models, fields

class TallerVisita(models.Model):
    _name = 'taller.visita'
    _description = 'Visita de Vehiculo al Taller'

    vehiculo_id = fields.Many2one('taller.vehiculo', string='Vehiculo', required=True)
    fecha = fields.Date(string='Fecha de la Visita', required=True)
    tipo_trabajo = fields.Selection([
        ('escaneo', 'Escaneo'),
        ('service', 'Service'),
        ('cambio_distribucion', 'Cambio de Distribucion'),
        ('otro', 'Otro'),
    ], string='Tipo de Trabajo', required=True)
    notas = fields.Text(string='Notas')
    piezas_usadas = fields.One2many('taller.visita.pieza', 'visita_id', string='Piezas Utilizadas')

