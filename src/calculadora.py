import re


def resolve_calculation(calc: str) -> int:
    """
    Calculadora que resolve operações matematicas simples, sem parenteses
    e somente com operadpres + - * /.

    Utiliza a função eval() para avaliar as contas.
    """
    if is_valid_calculation(calc):
        return eval(calc)
    raise ValueError('Invalid calculation')


def is_valid_calculation(calc: str) -> bool:
    SUM_MIN = r'[\+\-]'
    OPERATOR = r'[\+\-\*\/]'
    NUMBER = r'[0-9]+(\.[0-9]+)?'

    calc_match = re.match(
        # Start with an operator or a number
        rf'^(({SUM_MIN}{NUMBER})|{NUMBER})'
        # Followed by 0 or more operators and numbers
        rf'({OPERATOR}{NUMBER})*$',
        calc
    )

    return bool(calc_match)


if __name__ == '__main__':
    print(resolve_calculation('-1-2*3'))
