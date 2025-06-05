from odoo import models, fields

class TallerVehiculo(models.Model):
    _name = 'taller.vehiculo'
    _description = 'vehiculo del cliente'

    name = fields.Char(string='Patente', required=True)
    marca = fields.Char(string='Marca')
    modelo = fields.Char(string='Modelo')
    anio= fields.Char(string='Año')
    tipo_motor = fields.Char(string ='Tipo de motor')
    cliente_id = fields.Many2one('res.partner',string='Cliente')