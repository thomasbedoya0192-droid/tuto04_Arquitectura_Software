import datetime

class DummyPaymentProcessor:
    def procesar(self, monto):
        # Escribe automáticamente la línea de log en pagos_manuales.log
        with open("pagos_manuales.log", "a") as f:
            f.write(f"[{datetime.datetime.now()}] Pago procesado via API/Factory: ${monto}\n")
        return True

class PaymentFactory:
    @staticmethod
    def get_processor():
        return DummyPaymentProcessor()
