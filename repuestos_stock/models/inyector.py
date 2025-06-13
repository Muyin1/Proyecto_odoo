from odoo import models, fields

class Inyector(models.Model):
    _name = 'repuestos_stock.inyector'
    _description = "inyector"
    _inherit = "product.template"

    #campos especificos del inyector
    insulating_color = fields.Char(string = "Color Aislante")
    injection_type = fields.Selection([
        ('monopunto','Monopunto'),
        ('multipunto','Multipunto'),
    ], string="tipo de Inyeccion")

    #campos comunes a todos  los repuestos
    codigo_repuesto = fields.Char(string="Codigo de Repuesto", required=True, copy=False)
    codigo_oem = fields.Char(string="Coigo OEM")
    marca_id = fields.Many2one('repuestos_stock.marca', String ="Marca")
    vehiculo_ids = fields.Many2many('repuestos_stock.vehiculo', string='Vehiculos Compatibles')

    _sql_constraints = [
        ('unique_codigo_repuesto','UNIQUE(codigo_repuesto)',"El codigo del repuesto debe ser unico")
    ]

