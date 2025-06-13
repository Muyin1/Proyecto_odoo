from odoo import models, fields

class RepuestoBase(models.AbstractModel):
    _name = 'repuestos_stock.repuesto_base'
    _inherit = 'product.template'
    _description = 'Interfaz base para todos los repuestos'

    codigo_repuesto = fields.Char(string="Código de Repuesto", required=True, copy=False)
    codigo_oem = fields.Char(string="Código OEM")
    marca_id = fields.Many2one('repuestos_stock.marca', string="Marca", required=True)
    vehiculo_ids = fields.Many2many('repuestos_stock.vehiculo', string='Vehículos Compatibles')

    _sql_constraints = [
        ('unique_codigo_repuesto', 'unique(codigo_repuesto)', 'El código del repuesto debe ser único.'),
    ]
