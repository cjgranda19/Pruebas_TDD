# calc.py
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    elif n == 0:
        return 1
    return n * factorial(n - 1)

