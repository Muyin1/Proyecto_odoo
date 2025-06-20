from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = "product.template"

    # Campos ya existentes
    tipo_repuesto = fields.Selection([
        ('inyector', 'Inyector'),
        ('pastillas_freno', 'Pastillas de Freno'),
        ('sensor', 'Sensor'),
        ('alternador', 'Alternador'),
    ], string="Tipo de Repuesto", tracking=True)
    codigo_repuesto = fields.Char(string="Código de Repuesto", required=True, copy=False)
    codigo_oem = fields.Char(string="Código OEM")
    vehiculo_ids = fields.Many2many('repuestos_stock.vehiculo', string="Vehículos Compatibles")
    inyector_id = fields.One2many('repuesto.inyector', 'product_id', string="Ficha de Inyector")

    # Nuevo campo simple para marca
    marca = fields.Char(string='Marca')

    _sql_constraints = [
        ('unique_codigo_repuesto', 'UNIQUE(codigo_repuesto)', "El código del repuesto debe ser único.")
    ]

    @api.constrains('codigo_repuesto')
    def _check_codigo_repuesto(self):
        for record in self:
            if not record.codigo_repuesto:
                raise ValidationError("El código del repuesto es obligatorio.")
            duplicates = self.search([
                ('codigo_repuesto', '=', record.codigo_repuesto),
                ('id', '!=', record.id)
            ])
            if duplicates:
                raise ValidationError(f"El código {record.codigo_repuesto} ya existe en otro producto.")
