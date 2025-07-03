from odoo import models, fields, api

class TallerVehiculo(models.Model):
    _name = 'taller.vehiculo'
    _description = 'Vehículo del Cliente'

    name = fields.Char(string='Nombre', compute='_compute_name', store=True)
    partner_id = fields.Many2one('res.partner', string='Cliente', required=True)
    marca = fields.Char(string='Marca', required=True)
    modelo = fields.Char(string='Modelo', required=True)
    version = fields.Char(string="Version")
    anio = fields.Char(string='Año')
    tipo_motor = fields.Char(string='Tipo de Motor')
    patente = fields.Char(string='Patente', required=True)
    detalles = fields.Text(string='Detalles')
    kilometros = fields.Text(string="Kilometros")
    num_chasis = fields.Text(string = "Numero de Chasis / VIM ")
    codigo_motor = fields.Text(string="Codigo de Motor")


    @api.depends('partner_id', 'marca', 'modelo', 'patente')
    def _compute_name(self):
        for record in self:
            cliente = record.partner_id.name or ''
            marca = record.marca or ''
            modelo = record.modelo or ''
            patente = record.patente or ''
            record.name = f"{cliente} - {marca} {modelo} ({patente})"