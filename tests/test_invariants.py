"""Property-based testing for BLS12-381 mathematical invariants."""

import sys

from hypothesis import given, settings
from hypothesis import strategies as st
from py_ecc.optimized_bls12_381.optimized_curve import G1, G2, curve_order, multiply
from py_ecc.optimized_bls12_381.optimized_pairing import pairing

# Increase recursion depth significantly for pure-python py_ecc FQ12 operations
sys.setrecursionlimit(5000)


@settings(max_examples=5, deadline=None)
@given(
    a=st.integers(min_value=1, max_value=curve_order - 1),
    b=st.integers(min_value=1, max_value=curve_order - 1),
)
def test_pairing_linearity(a: int, b: int) -> None:
    """Test the linearity of the bilinear pairing: e(aP, bQ) == e(P, Q)^(ab).

    This verifies that the pairing implementation follows the expected
    mathematical properties across a wide range of scalar inputs.
    """
    p1 = multiply(G1, a)
    p2 = multiply(G2, b)

    # e(aP, bQ)
    pairing1 = pairing(p2, p1)

    # e(P, Q)^(ab)
    # Using the property: e(aP, Q) == e(P, aQ) == e(P, Q)^a
    p1_base = multiply(G1, (a * b) % curve_order)
    pairing2 = pairing(G2, p1_base)

    assert pairing1 == pairing2
