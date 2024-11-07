try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )

except ImportError as e:
    raise e

import unittest
from calculadora import soma, subtrai


class TesteCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5, 5), 10)  # ...ok

    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5, 5), 0)  # ...ok

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.5, 3.0),
            (-5, 5, 0),
            (100, 100, 200)
        )
        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):  # sub-testes
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)

    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        # gerenciador de contexto pra não falhar antes
        with self.assertRaises(AssertionError):
            # se colocar typeerror dá ruim no teste
            soma("11", 0)

###############################################################################
    def test_subtrai_5_e_5_deve_retornar_0(self):
        self.assertEqual(subtrai(5, 5), 0)

    def test_subtrai_0_e_10_deve_retornar_menos_10(self):
        self.assertEqual(subtrai(0, 10), -10)

    def test_subtrai_varias_entradas(self):
        a_b_subtrai_saidas = (
            (2, 1, 1),
            (0, 0, 0),
            (2, 2, 0),
            (1, 2, -1),
        )
        for a_b_subtrai_saida in a_b_subtrai_saidas:
            with self.subTest(a_b_subtrai_saida=a_b_subtrai_saida):
                a, b, subtrai_saida = a_b_subtrai_saida
                self.assertEqual(subtrai(a, b), subtrai_saida)

    def test_a_e_b_devem_ser_int_ou_float(self):
        with self.assertRaises(AssertionError):
            subtrai("a", "b")


if __name__ == "__main__":
    unittest.main(verbosity=2)
