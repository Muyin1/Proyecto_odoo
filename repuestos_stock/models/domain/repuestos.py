from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Repuesto(models.Model):
    _inherit = "product.template"

    # Clasificación del repuesto
    tipo_repuesto = fields.Selection([
        ('inyector', 'Inyector'),
        ('pastillas_freno', 'Pastillas de Freno'),
        ('regulador_presion', 'Regulador de Presion'),
        ('sensor_mariposa', 'Sensor de Posicion de Mariposas'),
        ('sensor_map','Sensor MAP'),
        ('sensor_rpm','Sensor de Rotacion / RPM'),
        ('sensor_maf','Sensor MAF'),
        ('motor_pasoapaso','Motor Paso a Paso'),
        # Podés seguir agregando tipos acá
    ], string="Tipo de Repuesto", tracking=True)

    #Punto de Venta siempre en True
    available_in_pos = fields.Boolean(default=True)

    #Campo para imagenes
    image_1920 = fields.Image()


    # Identificadores
    codigo_repuesto = fields.Char(string="Código de Repuesto", required=True, copy=False, default="Sin Codigo")
    codigo_oem = fields.Char(string="Código OEM", tracking=True)

    # Información general
    marca = fields.Char(string='Marca')
    vehiculo_ids = fields.Many2many(
        'repuestos_stock.vehiculo',
        string="Vehículos Compatibles"
    )

    #Conector con la ficha tecnica de cada repuesto
    ficha_tecnica_ids = fields.One2many('ficha.tecnica', 'producto_id', string='Ficha Técnica')


    #Campo para cargar stock inicial
    stock_inicial = fields.Float(string='Stock Inicial', help="Cantidad inicial en mano al momento de crear el repuesto")


    # Vinculacion de Prouductos equivalentes 
    producto_equivalente_ids = fields.Many2many(
        comodel_name = 'product.template',
        string='Equivalentes',
        compute='_compute_equivalentes',
        store = False
    )

    _sql_constraints = [
        ('unique_codigo_repuesto', 'unique(codigo_repuesto)', "El código del repuesto debe ser único.")
    ]


    #Api para codigo de Repuesto
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
    
    #Api para el control del stock
    @api.model
    def create(self,vals):
        stock_qty = vals.pop('stock_inicial', 0.0)
        producto = super().create(vals)

        if stock_qty > 0:
            producto._crear_movimiento_stock_inicial(stock_qty)

        return producto
    
    #Api para vinculacion por Codigo OEM
    @api.depends('codigo_oem')
    def _compute_equivalentes(self):
        for producto in self:
            if producto.codigo_oem:
                equivalentes = self.search([
                    ('codigo_oem', '=', producto.codigo_oem),
                    ('id', '!=', producto.id),
                    ('tipo_repuesto', '=', producto.tipo_repuesto)
                ])
                producto.producto_equivalente_ids = equivalentes
            else:
                producto.producto_equivalente_ids = False
    
    @api.model
    def create(self, vals):
        tipo = vals.get('tipo_repuesto')
        precio_base = vals.get('list_price', 0.0)

        # Lógica por tipo
        if tipo == 'inyector':
            # IVA 21% + margen 25%
            precio_final = precio_base * 1.21 * 1.25
        elif tipo == 'sensor_map':
            # IVA 10.5% + margen 15%
            precio_final = precio_base * 1.21 * 1.15
        elif tipo == 'pastillas_freno':
            # IVA 21% + margen 20%
            precio_final = precio_base * 1.21 * 1.20
        else:
            # Si no se reconoce, dejamos el precio original
            precio_final = precio_base

        vals['list_price'] = round(precio_final, 2)

        # Stock inicial
        stock_qty = vals.pop('stock_inicial', 0.0)
        producto = super().create(vals)

        if stock_qty > 0:
            producto._crear_movimiento_stock_inicial(stock_qty)

        return producto




    def _crear_movimiento_stock_inicial(self, cantidad):
        StockQuant = self.env['stock.quant'].sudo()
        Almacen = self.env['stock.warehouse'].search([('company_id', '=', self.env.company.id)], limit=1)

        location = Almacen.lot_stock_id or self.env.ref('stock.stock_location_stock')

        StockQuant.create({
            'product_id': self.product_variant_id.id,
            'location_id': location.id,
            'quantity': cantidad,
        })



class FichaTecnica(models.Model):
    _name = 'ficha.tecnica'
    _description = 'Ficha Técnica del Repuesto'

    producto_id = fields.Many2one('product.template', string='Repuesto')
    nombre = fields.Char(string='Nombre del atributo', required=True)
    valor = fields.Char(string='Valor')
