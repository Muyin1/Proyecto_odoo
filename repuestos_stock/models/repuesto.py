from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductTemplateAutoparte(models.Model):
    _inherit = "product.template"
    
    # Código único del repuesto.
    codigo_repuesto = fields.Char(
        string="Código",
        help="Código único del repuesto.",
        copy=False
    )
    
    # Código OEM (opcional).
    codigo_oem = fields.Char(
        string="Código OEM",
        help="Código OEM del repuesto (opcional)."
    )
    
    # Relación con la marca. Asegúrate de tener definido el modelo 'repuestos_stock.marca'.
    marca_id = fields.Many2one(
        'repuestos_stock.marca',
        string="Marca"
    )
    
    # Muchos a muchos con los vehículos compatibles.
    vehiculo_ids = fields.Many2many(
        'repuestos_stock.vehiculo',
        string="Vehículos compatibles"
    )
    
    # Tipo de repuesto, para relacionar piezas equivalentes entre distintas marcas.
    tipo_id = fields.Many2one(
        'repuestos_stock.tipo',
        string="Tipo de repuesto"
    )
    
    # Campo para el código de barras.
    barcode = fields.Char(
        string="Código de Barras",
        help="Código de barras (se puede cargar más adelante)."
    )
    
    # Restricción SQL para asegurar la unicidad del código del repuesto.
    _sql_constraints = [
        ('unique_codigo_repuesto', 'UNIQUE(codigo_repuesto)', "El código del repuesto debe ser único.")
    ]
    
    @api.constrains('codigo_repuesto')
    def _check_codigo_repuesto(self):
        for record in self:
            # Si no se carga el código, se considera un error en la carga inicial.
            if not record.codigo_repuesto:
                raise ValidationError("El código es obligatorio.")
            # Verifica duplicados en el mismo modelo.
            duplicates = self.search([
                ('codigo_repuesto', '=', record.codigo_repuesto),
                ('id', '!=', record.id)
            ])
            if duplicates:
                raise ValidationError(f"El código {record.codigo_repuesto} ya existe en otro producto.")
