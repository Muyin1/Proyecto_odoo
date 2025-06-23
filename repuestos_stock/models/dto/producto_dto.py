#ouputport interactua con templates

def producto_to_dto(producto):
    """Transforma un product.template en una estructura tipo DTO según su tipo de repuesto."""

    match producto.tipo_repuesto:
        case 'inyector':
            return {
                'id': producto.id,
                'codigo': producto.codigo_repuesto,
                'marca': producto.marca,
                'tipo': 'Inyector',
                'color_aislante': producto.insulating_color,
                'inyeccion': producto.injection_type,
                'pines': producto.number_pines,
            }