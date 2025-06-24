#Input port recibe datos y los envia a templates

from odoo.http import request

class CrearRepuesto:
    """Input Port responsable de crear un nuevo producto en base a los datos recibidos."""

    def crear(self, datos: dict):
        tipo = datos.get('tipo_repuesto')

        match tipo:
            case 'inyector':
                return self._crear_inyector(datos)
    
    #Crear un case para cada tipo
            

def _crear_inyector(self, datos):
        return request.env['product.template'].sudo().create({
            'codigo_repuesto': datos['codigo'],
            'codigo_oem': datos.get('oem'),
            'tipo_repuesto': 'inyector',
            'marca': datos.get('marca'),
            'insulating_color': datos.get('aislante'),
            'injection_type': datos.get('inyeccion'),
            'number_pines': datos.get('pines'),
        })

#Crear una funcion por cada tipo