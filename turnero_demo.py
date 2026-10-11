"""ALPHA93 / Turno Lab. Ejemplo educativo creado con asistencia de IA.

Ejecutar con Python 3. Usa datos ficticios; no asigna citas reales ni prioridad
clínica. No necesita dependencias, conexión, base de datos ni datos personales.
"""
from collections import deque


def asignar(solicitudes, horarios):
    """Asigna por llegada y devuelve asignaciones y solicitudes pendientes.

    Los originales no se modifican. Dos alias iguales siguen siendo solicitudes
    distintas. La falta de horarios conserva el resto de la fila.
    """
    fila = deque(solicitudes)
    asignaciones = []
    for horario in horarios:
        if not fila:
            break
        asignaciones.append((fila.popleft(), horario))
    return asignaciones, list(fila)


if __name__ == "__main__":
    turnos, pendientes = asignar(
        ["Solicitud A", "Solicitud B", "Solicitud C"], ["09:00", "09:15"]
    )
    print("DEMOSTRACIÓN ADMINISTRATIVA · DATOS FICTICIOS")
    for alias, horario in turnos:
        print(f"{alias} -> {horario}")
    print("Pendientes:", ", ".join(pendientes) or "ninguna")
