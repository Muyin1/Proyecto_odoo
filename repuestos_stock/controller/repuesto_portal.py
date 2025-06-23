#Controlador , epico

from odoo import http
from odoo.http import request
from ..models.services.create_repuesto import CrearRepuesto
from ..models.dto.producto_dto import producto_to_dto

class RepuestoController(http.Controller):
    #Controlador principal para operaciones sobre Repuestos vía API o portal

    # Ruta para crear un nuevo repuesto a través de una petición JSON.
    # Solo usuarios autenticados pueden usarlo (auth='user').
    @http.route('/api/repuestos/crear', type='json', auth='user')
    def crear_repuesto(self, **datos):
        try:
            # Usa la clase del InputPort para procesar la creación del producto.
            producto = CrearRepuesto().crear(datos)

            # Transforma el producto en un DTO para devolverlo limpio.
            dto = producto_to_dto(producto)

            return {
                'mensaje': 'Repuesto creado correctamente',
                'repuesto': dto,
            }

        except Exception as e:
            # En caso de error, devuelve el mensaje asociado.
            return {
                'error': str(e),
                'mensaje': 'No se pudo crear el repuesto'
            }

    # Ruta para listar todos los repuestos (o por tipo) como una API JSON.
    @http.route('/api/repuestos', type='json', auth='user')
    def listar_repuestos(self, tipo=None):
        domain = []
        if tipo:
            # Agrega un filtro si se pasa "tipo" por parámetro.
            domain.append(('tipo_repuesto', '=', tipo))

        # Busca todos los productos que cumplan con ese dominio.
        productos = request.env['product.template'].sudo().search(domain)

        # Convierte cada producto en una representación tipo DTO.
        dto_list = [producto_to_dto(p) for p in productos]

        return {
            'total': len(dto_list),
            'repuestos': dto_list
        }


class PortalRepuestoController(http.Controller):
    """
    Controlador para mostrar vistas web (QWeb) en el portal de usuario.
    """

    @http.route('/portal/repuestos', type='http', auth='user', website=True)
    def ver_repuestos_portal(self, **kw):
        productos = request.env['product.template'].sudo().search([])
        dto_list = [producto_to_dto(p) for p in productos]

        return request.render('repuestos_stock.portal_lista_repuestos', {
            'repuestos': dto_list
        })

    @http.route('/portal/inyectores', type='http', auth='user', website=True)
    def ver_inyectores_portal(self, **kw):
        productos = request.env['product.template'].sudo().search([
            ('tipo_repuesto', '=', 'inyector')
        ])
        dto_list = [producto_to_dto(p) for p in productos]

        return request.render('repuestos_stock.portal_lista_inyectores', {
            'inyectores': dto_list
        })
