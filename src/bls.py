"""BLS (Boneh-Lynn-Shacham) Signature Scheme Implementation.

This module provides a simple interface for generating BLS signatures and
verifying them using the BLS12-381 elliptic curve, following the
IETF BLS Signature specification (Proof of Possession variant).

Example:
    >>> from src.bls import BLS
    >>> sk, pk = BLS.key_gen()
    >>> message = b"hello world"
    >>> signature = BLS.sign(sk, message)
    >>> assert BLS.verify(pk, message, signature)
"""

import secrets
from typing import Sequence, Tuple, cast

from eth_typing import BLSPubkey, BLSSignature
from py_ecc.bls.ciphersuites import G2ProofOfPossession as bls_scheme
from py_ecc.bls12_381.bls12_381_curve import curve_order


class BLS:
    """BLS Signature Scheme wrapper for BLS12-381."""

    @staticmethod
    def key_gen() -> Tuple[int, bytes]:
        """Generate a random private key and its corresponding public key.

        The private key is a secure random integer in the range [1, curve_order-1].
        The public key is the result of G1 scalar multiplication.

        Returns:
            A tuple containing:
                - sk: The private key (integer).
                - pk: The public key (bytes, compressed).
        """
        # Securely generate a private key in the appropriate range
        sk = secrets.randbelow(curve_order - 1) + 1
        pk = bls_scheme.SkToPk(sk)
        return sk, pk

    @staticmethod
    def sign(sk: int, message: bytes) -> bytes:
        """Sign a message using the private key.

        Args:
            sk: The private key (integer).
            message: The message to sign (bytes).

        Returns:
            The signature (bytes, compressed).
        """
        return bls_scheme.Sign(sk, message)

    @staticmethod
    def verify(pk: bytes, message: bytes, signature: bytes) -> bool:
        """Verify a BLS signature.

        Args:
            pk: The public key (bytes, compressed).
            message: The message that was signed (bytes).
            signature: The signature to verify (bytes, compressed).

        Returns:
            True if the signature is valid, False otherwise.
        """
        try:
            return bls_scheme.Verify(
                cast(BLSPubkey, pk), message, cast(BLSSignature, signature)
            )
        except (ValueError, AssertionError):
            # py_ecc might raise errors on invalid point encodings or curve membership
            return False

    @staticmethod
    def aggregate_signatures(signatures: list[bytes]) -> bytes:
        """Aggregate multiple signatures into a single signature.

        Args:
            signatures: A list of signatures (bytes, compressed).

        Returns:
            The aggregated signature (bytes, compressed).
        """
        return bls_scheme.Aggregate(cast(Sequence[BLSSignature], signatures))

    @staticmethod
    def verify_aggregated(pks: list[bytes], message: bytes, agg_sig: bytes) -> bool:
        """Verify an aggregated signature for a single message.

        Args:
            pks: A list of public keys corresponding to the signers (bytes, compressed).
            message: The message that was signed by all (bytes).
            agg_sig: The aggregated signature (bytes, compressed).

        Returns:
            True if the aggregated signature is valid, False otherwise.
        """
        try:
            return bls_scheme.FastAggregateVerify(
                cast(Sequence[BLSPubkey], pks), message, cast(BLSSignature, agg_sig)
            )
        except (ValueError, AssertionError):
            return False
