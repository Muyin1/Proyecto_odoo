from odoo import models, fields, api

class Vehiculo(models.Model):
    _name = 'repuestos_stock.vehiculo'
    _description = 'Vehículo compatible con repuestos'

    marca = fields.Char(string='Marca', required=True)
    modelo = fields.Char(string='Modelo', required=True)
    version = fields.Char(string='Versión')  # Ej: Corolla Classic, Land Cruiser Prado
    motor = fields.Char(string='Motor')  # Ej: 1.4, 2.8, etc.
    codigo_motor = fields.Char(string='Código de Motor')  # Ej: 1KD-FTV, Z14XEP
    anios = fields.Char(string='Año', required=True)  # Año de salida

    name = fields.Char(string='Nombre completo', compute='_compute_name', store=True)

    @api.depends('marca', 'modelo', 'version', 'anio', 'motor', 'codigo_motor')
    def _compute_name(self):
        for record in self:
            partes = [record.marca, record.modelo]
            if record.version:
                partes.append(record.version)
            if record.anios:
                partes.append(f"({record.anios})")
            if record.motor:
                partes.append(f"({record.motor})")
            if record.codigo_motor:
                partes.append(f"[{record.codigo_motor}]")
            record.name = " ".join(partes)
