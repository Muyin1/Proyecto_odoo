from odoo import models, fields
import logging
_logger = logging.getLogger(__name__)
_logger.info("Cargando extensión de product.template en repuesto.py")


class RepuestoInyector(models.Model):
    _name = 'repuesto.inyector'
    _description = 'Datos del Inyector'

    product_id = fields.Many2one('product.template', string='Producto', ondelete='cascade', required=True)
    insulating_color = fields.Char(string="Color Aislante")
    injection_type = fields.Selection([
        ('monopunto', 'Monopunto'),
        ('multipunto', 'Multipunto'),
    ], string="Tipo de Inyección")

