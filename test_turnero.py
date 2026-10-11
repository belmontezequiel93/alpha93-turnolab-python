import unittest
from turnero_demo import asignar


class AsignarTests(unittest.TestCase):
    def test_fifo_y_pendientes(self):
        self.assertEqual(asignar(["A", "B", "C"], ["09:00", "09:15"]), ([("A", "09:00"), ("B", "09:15")], ["C"]))

    def test_no_modifica_originales(self):
        solicitudes = ["A", "B"]
        horarios = ["09:00"]
        asignar(solicitudes, horarios)
        self.assertEqual(solicitudes, ["A", "B"])
        self.assertEqual(horarios, ["09:00"])

    def test_sin_horarios(self):
        self.assertEqual(asignar(["A", "B"], []), ([], ["A", "B"]))

    def test_sin_solicitudes(self):
        self.assertEqual(asignar([], ["09:00"]), ([], []))

    def test_alias_repetidos(self):
        self.assertEqual(asignar(["A", "A"], ["09:00", "09:15"]), ([("A", "09:00"), ("A", "09:15")], []))

    def test_mas_horarios_que_solicitudes(self):
        self.assertEqual(asignar(["A"], ["09:00", "09:15"]), ([("A", "09:00")], []))


if __name__ == "__main__":
    unittest.main()
