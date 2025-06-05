from odoo import models, fields

class TallerVehiculo(models.Model):
    _name = 'taller.vehiculo'
    _description = 'Vehículo del Cliente'

    partner_id = fields.Many2one('res.partner', string='Cliente', required=True)
    marca = fields.Char(string='Marca', required=True)
    modelo = fields.Char(string='Modelo', required=True)
    anio = fields.Char(string='Año')
    tipo_motor = fields.Char(string='Tipo de Motor')
    patente = fields.Char(string='Patente')
    descripcion = fields.Text(string='Descripción')