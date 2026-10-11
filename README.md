# ALPHA93 · TurnoLab

Prototipo educativo en Python que asigna horarios a solicitudes ficticias por orden de llegada (FIFO). Forma parte del portfolio [ALPHA93](https://alpha93.com.ar/explorar.html#turnero) de Nelson Ezequiel Belmont.

## Qué demuestra

- Uso de `collections.deque` para conservar el orden de llegada.
- Separación entre asignaciones y solicitudes pendientes.
- Entradas originales sin modificaciones; alias repetidos como solicitudes distintas.
- Pruebas automatizadas sin dependencias externas.

## Ejecutar

Requiere Python 3. No necesita paquetes adicionales.

```sh
python turnero_demo.py
python -m unittest -v
```

Salida de la demostración:

```text
DEMOSTRACIÓN ADMINISTRATIVA · DATOS FICTICIOS
Solicitud A -> 09:00
Solicitud B -> 09:15
Pendientes: Solicitud C
```

## Alcance y límites

Ejemplo administrativo con datos ficticios. No gestiona citas reales ni utiliza datos de pacientes. No evalúa urgencia ni asigna prioridad clínica. El algoritmo es determinista y no usa IA para decidir el orden. El asistente del sitio explica el estado agregado de la simulación; ese backend no forma parte de este repositorio.

No se realizó una validación con un equipo de admisión. Este ejemplo sirve para aprender y mostrar el comportamiento FIFO, no como sistema hospitalario listo para uso real.

## Autoría

Proyecto del portfolio de Nelson Ezequiel Belmont, desarrollado con asistencia de IA.
