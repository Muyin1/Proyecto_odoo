from odoo import models, fields, api

class TallerVisita(models.Model):
    _name = 'taller.visita'
    _description = 'Visita de Vehiculo al Taller'

    name = fields.Char(string='Nombre', compute='_compute_name', store=True)
    vehiculo_id = fields.Many2one('taller.vehiculo', string='Vehiculo', required=True)
    fecha = fields.Date(string='Fecha de la Visita', required=True)
    fecha_salida = fields.Date(string='Fecha de Salida')
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('completado','Completado')
    ], string='Estado', default='pendiente')
    tipo_trabajo = fields.Selection([
        ('escaneo', 'Escaneo'),
        ('service', 'Service'),
        ('cambio_distribucion', 'Cambio de Distribucion'),
        ('otro', 'Otro'),
    ], string='Tipo de Trabajo', required=True)
    notas = fields.Text(string='Notas')
    piezas_usadas = fields.One2many('taller.visita.pieza', 'visita_id', string='Piezas Utilizadas')

    @api.depends('vehiculo_id', 'fecha', 'tipo_trabajo')
    def _compute_name(self):
        for record in self:
            vehiculo = record.vehiculo_id
            cliente = vehiculo.partner_id.name if vehiculo.partner_id else 'Cliente'
            marca_modelo = f"{vehiculo.marca or ''} {vehiculo.modelo or ''}".strip()
            patente = vehiculo.patente or ''
            fecha = record.fecha.strftime('%d/%m/%Y') if record.fecha else ''
            trabajo = dict(self.fields['tipo_trabajo'].selection).get(record.tipo_trabajo, '')
            record.name = f"{cliente} - {marca_modelo} ({patente}) - {trabajo} - {fecha}"