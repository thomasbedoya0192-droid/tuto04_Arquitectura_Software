from tienda_app.models import Libro

class CompraService:
    def __init__(self, procesador_pago):
        self.procesador_pago = procesador_pago

    def ejecutar_compra(self, libro_id, direccion, usuario=None):
        try:
            libro = Libro.objects.get(id=libro_id)
        except Libro.DoesNotExist:
            raise ValueError("El libro especificado no existe.")

        if libro.stock_actual <= 0:
            raise ValueError("Sin stock disponible.")

        # Llama al procesador que escribe en el log
        self.procesador_pago.procesar(libro.precio)
        
        # Descuenta el inventario
        libro.stock_actual -= 1
        libro.save()

        return libro.precio
