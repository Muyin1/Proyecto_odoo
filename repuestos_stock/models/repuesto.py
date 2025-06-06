from odoo import models, fields

class Repuesto(models.Model):
    _name = 'repuestos_stock.repuesto'
    _description = 'Repuesto del taller'

    marca_id = fields.Many2one('repuestos_stock.marca', string='marca', required=True)
    codigo = fields.Char(string='Codigo', required=True, unique=True)
    codigo_oem = fields.Char(string='Codigo OEM')
    vehiculo_ids = fields.Many2many('repuestos_stock.vehiculo', string='Vehículos compatibles')
    descripcion = fields.Char(string='Descripcion')
    cantidad = fields.Integer(string='Cantidad en stock', default=0)
    precio_venta = fields.Float(string='Precio de venta')