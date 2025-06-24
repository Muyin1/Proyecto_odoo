from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Repuesto(models.Model):
    _inherit = "product.template"

    # Clasificación del repuesto
    tipo_repuesto = fields.Selection([
        ('inyector', 'Inyector'),
        ('pastillas_freno', 'Pastillas de Freno'),
        ('sensor', 'Sensor'),
        ('alternador', 'Alternador'),
        # Podés seguir agregando tipos acá
    ], string="Tipo de Repuesto", tracking=True)

    # Identificadores
    codigo_repuesto = fields.Char(string="Código de Repuesto", required=True, copy=False, default="Sin Codigo")
    codigo_oem = fields.Char(string="Código OEM", tracking=True)

    # Información general
    marca = fields.Char(string='Marca')
    vehiculo_ids = fields.Many2many(
        'repuestos_stock.vehiculo',
        string="Vehículos Compatibles"
    )

    # Atributos específicos — para inyectores
    insulating_color = fields.Char(string="Color del Aislante")
    injection_type = fields.Selection([
        ('monopunto', 'Monopunto'),
        ('multipunto', 'Multipunto'),
    ], string="Tipo de Inyección")
    number_pines = fields.Char(string="Cantidad de Pines")

    # Podés seguir agregando campos para otros tipos acá (sensor, alternador, etc.)

    _sql_constraints = [
        ('unique_codigo_repuesto', 'unique(codigo_repuesto)', "El código del repuesto debe ser único.")
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
