"""Tests para la función sub(a, b) -> float."""

import pytest

from src.calculator import sub


# --- EJEMPLO (no borrar) ---
def test_sub_resta_positivos():
    """Ejemplo: 5 - 2 debe dar 3."""
    assert sub(5, 2) == 3


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Restar un número mayor al primero (resultado negativo)
#   - Restar cero
#   - Restar dos números negativos
#   - Restar dos números decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (3, 5, -2),
        (8, 0, 8),
        (-3, -5, 2),
        (5.5, 2.2, 3.3),
    ],
)
def test_sub_casos_pedidos(a, b, expected):
    assert sub(a, b) == pytest.approx(expected)
