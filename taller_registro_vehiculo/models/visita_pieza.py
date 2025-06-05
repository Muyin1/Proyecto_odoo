from odoo import models, fields

class TallerVisitaPieza(models.Model):
    _name = 'taller.visita.pieza'
    _description = 'Pieza utlizada en la visita'

    visita_id = fields.Many2one('taller.visita', string='Visita')
    marca = fields.Char(string='Marca de la Pieza')
    codigo_pieza = fields.Char(string='Codigo de Pieza')
    descripcion = fields.Text(string='Descripcion')
    