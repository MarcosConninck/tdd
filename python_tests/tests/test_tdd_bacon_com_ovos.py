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
from tdd_bacon_com_ovos import bacon_com_ovos


class TestBaconComOvos(unittest.TestCase):
    def test_deve_levantar_assertionerror_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('a')

    def test_argumento_multiplo_de_3_e_5_retornar_bacon_com_ovos(self):
        entradas = (15, 30, 45, 60)
        saida = 'bacon com ovos'
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'entrada: {entrada} não retornou {saida}')

    def test_argumento_nao_multiplo_de_3_e_5_retornar_passa_fome(self):
        entradas = (1, 31, 44, 71)
        saida = 'passa fome'
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'entrada: {entrada} não retornou {saida}')

    def test_argumento_multiplo_de_3_retornar_bacon(self):
        entradas = (3, 6, 9, 33)
        saida = 'bacon'
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'entrada: {entrada} não retornou {saida}')

    def test_argumento_multiplo_de_5_retornar_ovos(self):
        entradas = (5, 10, 20, 35)
        saida = 'ovos'
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'entrada: {entrada} não retornou {saida}')


if __name__ == "__main__":
    unittest.main(verbosity=2)
