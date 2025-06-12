from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    _inherit = "product.template"

    tipo_repuesto = fields.Selection([
        ('inyector', 'Inyector'),
        ('pastillas_freno', 'Pastillas de Freno'),
        ('sensor', 'Sensor'),
        ('alternador', 'Alternador'),
    ], string="Tipo de Repuesto")
    
    # Campos específicos según tipo de repuesto
    codigo_repuesto = fields.Char(string="Código de Repuesto", required=True, copy=False)
    marca_id = fields.Many2one('repuestos_stock.marca', string="Marca")
    codigo_oem = fields.Char(string="Código OEM")
    
    # Datos solo para inyectores
    insulating_color = fields.Char(string="Color Aislante")
    injection_type = fields.Selection([
        ('monopunto', 'Monopunto'),
        ('multipunto', 'Multipunto'),
    ], string="Tipo de Inyección")
    
    # Datos solo para pastillas de freno
    material = fields.Selection([
        ('ceramico', 'Cerámico'),
        ('metalico', 'Metálico'),
        ('organico', 'Orgánico'),
    ], string="Material de Pastilla")
    espesor = fields.Float(string="Espesor (mm)")
    
    # Compatibilidad con vehículos
    vehiculo_ids = fields.Many2many('repuestos_stock.vehiculo', string="Vehículos Compatibles")
    
    # Restricción SQL para asegurar la unicidad del código del repuesto.
    _sql_constraints = [
        ('unique_codigo_repuesto', 'UNIQUE(codigo_repuesto)', "El código del repuesto debe ser único.")
    ]
    
    @api.constrains('codigo_repuesto')
    def _check_codigo_repuesto(self):
        for record in self:
            if not record.codigo_repuesto:
                raise ValidationError("El código de repuesto es obligatorio.")
            
            # Verifica duplicados en el modelo product.template
            duplicates = self.search([
                ('codigo_repuesto', '=', record.codigo_repuesto),
                ('id', '!=', record.id)
            ])
            if duplicates:
                raise ValidationError(f"El código {record.codigo_repuesto} ya existe en otro producto.")

