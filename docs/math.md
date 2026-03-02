# Mathematical Context

## BLS12-381 Elliptic Curve

The implementations within this template utilize the BLS12-381 elliptic curve, which is widely adopted in modern blockchain systems for pairing-based signatures and zero-knowledge proofs.

### Bilinear Pairings

A bilinear pairing is a function $e: \mathbb{G}_1 	imes \mathbb{G}_2 	o \mathbb{G}_T$ with the following properties:

1.  **Bilinearity:** $e(aP, bQ) = e(P, Q)^{ab}$ for all $P \in \mathbb{G}_1, Q \in \mathbb{G}_2$ and $a, b \in \mathbb{Z}$.
2.  **Non-degeneracy:** If $P$ and $Q$ are generators, then $e(P, Q)$ is a generator of $\mathbb{G}_T$.
3.  **Efficiency:** The pairing $e(P, Q)$ can be computed efficiently.

### Security Assumptions

The security of the protocols implemented within this framework typically relies on one or more of the following:

- **Computational Diffie-Hellman (CDH) Assumption:** Given $P, aP, bP \in \mathbb{G}$, it is computationally infeasible to compute $abP$.
- **Decisional Bilinear Diffie-Hellman (DBDH) Assumption:** Given $P, aP, bP, cP \in \mathbb{G}$, it is computationally infeasible to distinguish $e(P, P)^{abc}$ from a random element in $\mathbb{G}_T$.
- **Random Oracle Model (ROM):** The hash function used to map messages to curve points is treated as a truly random function.

## BLS Signatures

The Boneh-Lynn-Shacham (BLS) signature scheme consists of three algorithms:

1.  **KeyGen:** Select a random scalar $sk \in \mathbb{Z}_r$ and compute the public key $pk = sk \cdot P_1$.
2.  **Sign:** Compute the signature $\sigma = sk \cdot H(m)$, where $H: \{0,1\}^* 	o \mathbb{G}_2$ is a hash-to-curve function.
3.  **Verify:** Check if $e(P_1, \sigma) = e(pk, H(m))$.
