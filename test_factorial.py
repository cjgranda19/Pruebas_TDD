# test_factorial.py

# Importa la función `factorial` desde el módulo calc.py
from calc import factorial

def test_factorial_de_cero():
    """
    Caso de prueba 1: Factorial de 0.
    Según la definición matemática, 0! = 1.
    """
    # Llama a factorial(0) y comprueba que devuelve 1
    assert factorial(0) == 1

def test_factorial_de_cinco():
    """
    Caso de prueba 2: Factorial de 5.
    Matemáticamente, 5! = 5 × 4 × 3 × 2 × 1 = 120.
    """
    # Llama a factorial(5) y comprueba que devuelve 120
    assert factorial(5) == 120

