"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Multiplicar por cero
#   - Multiplicar dos números negativos (resultado positivo)
#   - Multiplicar un positivo y un negativo (resultado negativo)
#   - Multiplicar por 1 (elemento neutro)
#   - Multiplicar dos decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (9, 0, 0),
        (-3, -5, 15),
        (4, -3, -12),
        (7, 1, 7),
        (1.5, 2.2, 3.3),
    ],
)
def test_mul_casos_pedidos(a, b, expected):
    assert mul(a, b) == pytest.approx(expected)
