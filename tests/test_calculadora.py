# adicionar src ao path
try:
    import os
    import sys

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src/'
            )
        )
    )
except:
    raise ImportError()


# testes
import unittest
from calculadora import resolve_calculation, is_valid_calculation


class CalculadoraTest(unittest.TestCase):
    def test_is_valid_calculation_deve_retornar_false_se_forem_enviadas_contas_invalidas(self):
        entradas = ['a+21', '#', '@*54', '!1',
                    '%*', '++2', '1=2', '1--3', '*22']

        for entrada in entradas:
            self.assertFalse(is_valid_calculation(entrada))

    def test_is_valid_calculation_deve_retornar_true_se_forem_enviados_numeros_ou_operadores(self):
        entradas = ['1+22', '-1-1', '1*2', '11/2',
                    '1+22+3', '1-2-3', '12*2*3', '1/2/3']

        for entrada in entradas:
            self.assertTrue(is_valid_calculation(entrada))

    def test_resolve_calculation_deve_retornar_o_resultado_de_uma_conta_valida(self):
        conta_resultado = [('1+22', 23), ('1-22', -21),
                           ('2*22', 44), ('22/2', 11)]

        for conta, resultado in conta_resultado:
            self.assertEqual(resolve_calculation(conta), resultado)

    def test_resolve_calculation_deve_lancar_ValueError_se_for_enviada_conta_invalida(self):
        entradas = ['a+22', '#', '@*5', '!1', '%*',
                    '++2', '11=2', '1--3', '*2-3', '23++1']

        for entrada in entradas:
            with self.assertRaises(ValueError):
                resolve_calculation(entrada)


if __name__ == '__main__':
    unittest.main()
