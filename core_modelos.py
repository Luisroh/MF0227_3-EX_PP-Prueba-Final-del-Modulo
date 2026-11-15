# core_modelos.py

class EstadoInvalidoError(Exception):
    """Excepción lanzada cuando se intenta una transición de estado no permitida."""
    pass


class TicketTecnico:
    # Estados permitidos
    ABIERTO = "Abierto"
    EN_PROCESO = "En Proceso"
    CERRADO = "Cerrado"

    # Transiciones válidas: estado_actual -> [estados_permitidos]
    _TRANSICIONES = {
        ABIERTO: [EN_PROCESO, CERRADO],
        EN_PROCESO: [CERRADO],
        CERRADO: [], 
    }

    def __init__(self, id_ticket, titulo, prioridad):
        self._id = id_ticket
        self._titulo = titulo
        self._estado = self.ABIERTO
        self._prioridad = prioridad  # "Alta", "Media", "Baja"

    @property
    def estado(self):
        return self._estado

    @property
    def prioridad(self):
        return self._prioridad

    def cambiar_estado(self, nuevo_estado):
        """Valida la transición antes de cambiar el estado."""
        if nuevo_estado not in self._TRANSICIONES[self._estado]:
            raise EstadoInvalidoError(
                f"No se puede pasar de '{self._estado}' a '{nuevo_estado}'."
            )
        self._estado = nuevo_estado

    def calcular_sla(self):
        """Método base. Las hijas lo sobrescriben (polimorfismo)."""
        raise NotImplementedError("Las subclases deben implementar calcular_sla()")


class TicketHardware(TicketTecnico):
    def __init__(self, id_ticket, titulo, prioridad, componente):
        super().__init__(id_ticket, titulo, prioridad)
        self.componente = componente

    def calcular_sla(self):
        # SLA en horas según prioridad para Hardware
        tabla = {"Alta": 4, "Media": 12, "Baja": 24}
        return tabla.get(self.prioridad, 24)


class TicketSoftware(TicketTecnico):
    def __init__(self, id_ticket, titulo, prioridad, sistema_operativo):
        super().__init__(id_ticket, titulo, prioridad)
        self.sistema_operativo = sistema_operativo

    def calcular_sla(self):
        # SLA en horas según prioridad para Software
        tabla = {"Alta": 8, "Media": 24, "Baja": 48}
        return tabla.get(self.prioridad, 48)


if __name__ == "__main__":
    print("=== Pruebas de POO ===")

    # Instancia Hardware
    hw = TicketHardware(1, "Pantalla rota", "Alta", "Monitor")
    print(f"Ticket HW: {hw._titulo}, SLA: {hw.calcular_sla()}h")

    # Instancia Software
    sw = TicketSoftware(2, "Error en Office", "Media", "Windows 11")
    print(f"Ticket SW: {sw._titulo}, SLA: {sw.calcular_sla()}h")

    # Prueba de transición válida
    hw.cambiar_estado(TicketTecnico.EN_PROCESO)
    print(f"HW estado tras cambio: {hw.estado}")

    # Prueba de transición inválida (debe lanzar excepción)
    try:
        sw.cambiar_estado(TicketTecnico.CERRADO)
        sw.cambiar_estado(TicketTecnico.EN_PROCESO)  # Debe fallar
    except EstadoInvalidoError as e:
        print(f"Excepción capturada correctamente: {e}")