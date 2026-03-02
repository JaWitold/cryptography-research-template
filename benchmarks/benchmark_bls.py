"""Benchmarking suite for BLS Signature operations."""

import timeit

from src.bls import BLS


def benchmark_key_gen(iterations: int = 100) -> None:
    """Measure the time taken for key generation."""
    timer = timeit.Timer(lambda: BLS.key_gen())
    avg_time = timer.timeit(number=iterations) / iterations
    print(f"Key Generation: {avg_time * 1000:.3f} ms / op")


def benchmark_signing(iterations: int = 100) -> None:
    """Measure the time taken for signing."""
    sk, _ = BLS.key_gen()
    message = b"Research data to be signed"
    timer = timeit.Timer(lambda: BLS.sign(sk, message))
    avg_time = timer.timeit(number=iterations) / iterations
    print(f"Signing: {avg_time * 1000:.3f} ms / op")


def benchmark_verification(iterations: int = 100) -> None:
    """Measure the time taken for verification."""
    sk, pk = BLS.key_gen()
    message = b"Research data to be signed"
    signature = BLS.sign(sk, message)
    timer = timeit.Timer(lambda: BLS.verify(pk, message, signature))
    avg_time = timer.timeit(number=iterations) / iterations
    print(f"Verification: {avg_time * 1000:.3f} ms / op")


def benchmark_aggregation(n_signers: int = 10, iterations: int = 10) -> None:
    """Measure the time taken for aggregation and batch verification."""
    message = b"Collective agreement message"
    signers = [BLS.key_gen() for _ in range(n_signers)]
    signatures = [BLS.sign(sk, message) for sk, pk in signers]
    pks = [pk for sk, pk in signers]

    # Benchmark aggregation
    agg_timer = timeit.Timer(lambda: BLS.aggregate_signatures(signatures))
    avg_agg_time = agg_timer.timeit(number=iterations) / iterations

    # Benchmark verification
    agg_sig = BLS.aggregate_signatures(signatures)
    verify_timer = timeit.Timer(lambda: BLS.verify_aggregated(pks, message, agg_sig))
    avg_verify_time = verify_timer.timeit(number=iterations) / iterations

    print(f"Aggregation ({n_signers} signers): {avg_agg_time * 1000:.3f} ms / op")
    print(f"Aggregated Verify ({n_signers} pks): {avg_verify_time * 1000:.3f} ms / op")


if __name__ == "__main__":
    print("Starting BLS benchmarks...")
    benchmark_key_gen()
    benchmark_signing()
    benchmark_verification()
    benchmark_aggregation()
    print("Benchmark complete.")
