from odoo import http
from odoo.http import request

class RepuestoPortal(http.Controller):

    @http.route('/mis-repuestos', type='http', auth='public', website=True)
    def ver_repuestos(self, tipo=None, **kw):
        domain = []
        if tipo:
            domain.append(('tipo_repuesto', '=', tipo))

        productos = request.env['product.template'].sudo().search(domain)

        tipos = request.env['product.template'].sudo().read_group(
            [('tipo_repuesto', '!=', False)],
            ['tipo_repuesto'],
            ['tipo_repuesto']
        )
        return request.render('repuestos_stock.portal_lista_repuestos', {
            'productos': productos,
            'tipos': [t['tipo_repuesto'] for t in tipos],
            'tipo_seleccionado': tipo,
        })
