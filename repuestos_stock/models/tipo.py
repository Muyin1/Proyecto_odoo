from odoo import models, fields

class TipoRepuesto(models.Model):
    _name = 'repuestos_stock.tipo'
    _description = 'Tipo de Repuesto'

    name = fields.Char(string='Nombre del Tipo', required=True, translate=True)
    descripcion = fields.Text(string='Descripción')
