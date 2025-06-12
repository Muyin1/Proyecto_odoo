from odoo import models, fields, api
from odoo.exceptions import ValidationError

# Heredamos el modelo de productos para agregarle campos nuevos
class ProductTemplate(models.Model):
    _inherit = "product.template"

    # Tipo de repuesto, sirve para identificar su categoría
    tipo_repuesto = fields.Selection([
        ('inyector', 'Inyector'),
        ('pastillas_freno', 'Pastillas de Freno'),
        ('sensor', 'Sensor'),
        ('alternador', 'Alternador'),
    ], string="Tipo de Repuesto")
    
    # Código interno del repuesto (único)
    codigo_repuesto = fields.Char(string="Código de Repuesto", copy=False)

    # Marca del repuesto (relación con el modelo repuestos_stock.marca)
    marca_id = fields.Many2one('repuestos_stock.marca', string="Marca")     

    # Código original del fabricante
    codigo_oem = fields.Char(string="Código OEM")
    
    # Solo para inyectores
    insulating_color = fields.Char(string="Color Aislante")
    injection_type = fields.Selection([
        ('monopunto', 'Monopunto'),
        ('multipunto', 'Multipunto'),
    ], string="Tipo de Inyección")

    # Solo para pastillas de freno
    material = fields.Selection([
        ('ceramico', 'Cerámico'),
        ('metalico', 'Metálico'),
        ('organico', 'Orgánico'),
    ], string="Material de Pastilla")
    espesor = fields.Float(string="Espesor (mm)")

    # Relación con vehículos compatibles (many2many)
    vehiculo_ids = fields.Many2many('repuestos_stock.vehiculo', string="Vehículos Compatibles")
    
    # Restricción de base de datos: no se pueden repetir códigos de repuesto
    _sql_constraints = [
        ('unique_codigo_repuesto', 'UNIQUE(codigo_repuesto)', "El código del repuesto debe ser único.")
    ]

    # Validación adicional: chequea duplicados manualmente al guardar
    @api.constrains('codigo_repuesto')
    def _check_codigo_repuesto(self):
        for record in self:
            # Si hay código cargado, busca duplicados
            if record.codigo_repuesto:
                duplicates = self.search([
                    ('codigo_repuesto', '=', record.codigo_repuesto),
                    ('id', '!=', record.id)  # Excluye el propio registro
                ])
                if duplicates:
                    raise ValidationError(f"El código {record.codigo_repuesto} ya existe en otro producto.")
