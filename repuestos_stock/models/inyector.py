from odoo import models, fields

class RepuestoInyector(models.Model):
    _name = 'repuesto.inyector'
    _description = 'Datos del Inyector'

    product_id = fields.Many2one('product.template', string='Producto', ondelete='cascade', required=True)
    insulating_color = fields.Char(string="Color Aislante")
    injection_type = fields.Selection([
        ('monopunto', 'Monopunto'),
        ('multipunto', 'Multipunto'),
    ], string="Tipo de Inyección")


