from odoo import models, fields,api
from odoo.exceptions import ValidationError

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

    _sql_contraints = [
        ('unique_codigo_repuesto','UNIQUE(codigo)','El código del repuesto debe ser único.')
    ] 
    
    @api.Model
    def create(self, vals):
        if self.search([('codigo','=', vals.get('codigo'))]):
            codigo = vals.get("codigo")
            raise ValidationError(f'El repuesto con código {codigo} ya existe.')
        return super(Repuesto, self).create(vals)