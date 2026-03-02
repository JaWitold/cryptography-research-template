"""Global configuration for the cryptography research template."""

import enum


class SecurityLevel(enum.Enum):
    """Supported security levels for research and testing."""

    TEST = "test"
    RESEARCH = "research"


class Config:
    """Security parameters and cryptographic constants."""

    # Default security level
    LEVEL = SecurityLevel.RESEARCH

    # Elliptic Curve: BLS12-381
    # Security Level: ~128 bits
    CURVE_NAME = "BLS12-381"

    # Pairing targets
    G1_COMPRESSED_SIZE = 48
    G2_COMPRESSED_SIZE = 96

    @property
    def is_research_mode(self) -> bool:
        """Check if the system is in research mode."""
        return self.LEVEL == SecurityLevel.RESEARCH
