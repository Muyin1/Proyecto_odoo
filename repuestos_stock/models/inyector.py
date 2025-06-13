from odoo import models, fields

class Inyector(models.Model):
    _name = 'repuestos_stock.inyector'
    _description = 'Inyector'
    _inherit = 'repuestos_stock.repuesto_base'

    insulating_color = fields.Char(string="Color Aislante")
    injection_type = fields.Selection([
        ('monopunto', 'Monopunto'),
        ('multipunto', 'Multipunto'),
    ], string="Tipo de Inyección")
