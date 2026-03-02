"""Tests for the BLS Signature implementation."""

import secrets
from unittest.mock import patch

from src.bls import BLS


def test_key_gen() -> None:
    """Test private and public key generation."""
    sk, pk = BLS.key_gen()
    assert isinstance(sk, int)
    assert (
        1 <= sk < 0x73EDA7532F9278980C8EC231857C2452E7999110308DBADB3452818452063F01
    )  # BLS12-381 curve order
    assert isinstance(pk, bytes)
    assert len(pk) == 48  # Compressed G1 point size


def test_sign_verify_success() -> None:
    """Test a basic sign and verify workflow (success)."""
    sk, pk = BLS.key_gen()
    message = b"I am signing this message with BLS"
    signature = BLS.sign(sk, message)
    assert isinstance(signature, bytes)
    assert len(signature) == 96  # Compressed G2 point size
    assert BLS.verify(pk, message, signature) is True


def test_verify_fail_wrong_message() -> None:
    """Test verification fail with a modified message."""
    sk, pk = BLS.key_gen()
    message = b"I am signing this message with BLS"
    signature = BLS.sign(sk, message)
    wrong_message = b"Different message"
    assert BLS.verify(pk, wrong_message, signature) is False


def test_verify_fail_wrong_pk() -> None:
    """Test verification fail with a different public key."""
    sk, pk = BLS.key_gen()
    _, other_pk = BLS.key_gen()
    message = b"I am signing this message with BLS"
    signature = BLS.sign(sk, message)
    assert BLS.verify(other_pk, message, signature) is False


def test_verify_fail_invalid_signature() -> None:
    """Test verification fail with a malformed or unrelated signature."""
    sk, pk = BLS.key_gen()
    message = b"I am signing this message with BLS"

    # Create an invalid signature of the correct length (96 bytes)
    invalid_sig = secrets.token_bytes(96)
    assert BLS.verify(pk, message, invalid_sig) is False


def test_aggregate_signatures() -> None:
    """Test signature aggregation and batch verification."""
    message = b"I am signing this message with BLS"
    signers = [BLS.key_gen() for _ in range(5)]
    signatures = [BLS.sign(sk, message) for sk, pk in signers]
    pks = [pk for sk, pk in signers]

    agg_sig = BLS.aggregate_signatures(signatures)
    assert BLS.verify_aggregated(pks, message, agg_sig) is True


def test_verify_aggregated_fail() -> None:
    """Test aggregated signature verification failure."""
    message = b"I am signing this message with BLS"
    signers = [BLS.key_gen() for _ in range(3)]
    signatures = [BLS.sign(sk, message) for sk, pk in signers]
    pks = [pk for sk, pk in signers]

    # Use only some signatures for the aggregate
    agg_sig = BLS.aggregate_signatures(signatures[:-1])
    # Attempt to verify with all public keys
    assert BLS.verify_aggregated(pks, message, agg_sig) is False


def test_verify_exception_handling() -> None:
    """Test exception handling in verify."""
    with patch("py_ecc.bls.G2ProofOfPossession.Verify", side_effect=ValueError):
        assert BLS.verify(b"pk", b"m", b"s") is False


def test_verify_aggregated_exception_handling() -> None:
    """Test exception handling in verify_aggregated."""
    with patch(
        "py_ecc.bls.G2ProofOfPossession.FastAggregateVerify", side_effect=AssertionError
    ):
        assert BLS.verify_aggregated([b"pk"], b"m", b"s") is False
