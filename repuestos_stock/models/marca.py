from odoo import models, fields

class MarcaRepuesto(models.Model):
    _name = 'repuestos_stock.marca'
    _description = 'Marca de Repuesto'

    name = fields.Char(string='Nombre de la Marca', required=True, translate=True)
    descripcion = fields.Text(string='Descripcion')
    activo = fields.Boolean(string='Activo', default=True)

    repuesto_ids = fields.One2many('repuestos_stock.repuesto','marca_id', string='Repuestos')
    