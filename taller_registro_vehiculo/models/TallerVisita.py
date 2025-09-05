from odoo import models, fields, api

class TallerVisita(models.Model):
    # --- CAMBIO 1: Heredar de 'mail.thread' y 'mail.activity.mixin' ---
    _name = 'taller.visita'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Visita de Vehiculo al Taller'

    company_id = fields.Many2one('res.company', string='Compañía', required=True, default=lambda self: self.env.company)
    name = fields.Char(string='Nombre', compute='_compute_name', store=True)
    vehiculo_id = fields.Many2one('taller.vehiculo', string='Vehiculo', required=True)
    kilometros = fields.Char(string='Kilometros',required=True)
    fecha = fields.Date(string='Fecha de la Visita', required=True)
    fecha_salida = fields.Date(string='Fecha de Salida')
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_proceso','En Proceso'),
        ('completado','Completado'),
    ], string='Estado', default='pendiente', tracking=True)
    
    # --- LÍNEA CORREGIDA ---
    tipo_trabajo = fields.Selection([
        ('escaneo', 'Escaneo'),
        ('service', 'Service'),
        ('cambio_distribucion', 'Cambio de Distribucion'),
        ('cambio_amortiguador','Cambio de Amortiguador'),
        ('otro', 'Otro'),
    ], string='Tipo de Trabajo', required=True)
    
    notas = fields.Text(string='Notas')
    piezas_usadas = fields.One2many('taller.visita.pieza', 'visita_id', string='Piezas Utilizadas')
    
    partner_id = fields.Many2one(related='vehiculo_id.partner_id', string='Cliente', store=True)
    marca = fields.Char(related='vehiculo_id.marca', string='Marca', store=True)
    modelo = fields.Char(related='vehiculo_id.modelo', string='Modelo', store=True)
    patente = fields.Char(related='vehiculo_id.patente', string='Patente', store=True)

    @api.depends('vehiculo_id', 'tipo_trabajo', 'fecha')
    def _compute_name(self):
        for record in self:
            trabajo_label = dict(self._fields['tipo_trabajo'].selection).get(record.tipo_trabajo, '')
            record.name = f"{record.vehiculo_id.name or ''} - {trabajo_label} - {record.fecha.strftime('%Y-%m-%d') if record.fecha else ''}"

    @api.model_create_multi
    def create(self, vals_list):
        visitas = super().create(vals_list)
        
        # El nombre del módulo debe coincidir con el de tu carpeta (ej: 'taller_registro_vehiculo')
        notification_group = self.env.ref('taller_registro_vehiculo.group_taller_notificaciones', raise_if_not_found=False)
        
        if notification_group:
            users_to_notify = notification_group.users
            
            for visita in visitas:
                if visita.estado == 'pendiente':
                    activity_data = {
                        'activity_type_id': self.env.ref('mail.mail_activity_data_todo').id,
                        'summary': f"Nuevo trabajo pendiente: {visita.name}",
                        'note': f"Se ha registrado un nuevo trabajo para el vehículo {visita.patente}. Por favor, revisar.",
                        'date_deadline': visita.fecha,
                    }
                    
                    for user in users_to_notify:
                        activity_data['user_id'] = user.id
                        visita.activity_schedule(**activity_data)
                        
        return visitas