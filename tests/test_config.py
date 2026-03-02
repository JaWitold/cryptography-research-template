"""Tests for the global configuration."""

from src.config import Config, SecurityLevel


def test_config_constants() -> None:
    """Test that configuration constants are correctly defined."""
    assert Config.CURVE_NAME == "BLS12-381"
    assert Config.G1_COMPRESSED_SIZE == 48
    assert Config.G2_COMPRESSED_SIZE == 96


def test_is_research_mode() -> None:
    """Test the is_research_mode property logic."""
    config = Config()

    # Default should be RESEARCH based on src/config.py
    assert Config.LEVEL == SecurityLevel.RESEARCH
    assert config.is_research_mode is True


def test_security_level_enum() -> None:
    """Test the SecurityLevel enum values."""
    assert SecurityLevel.TEST.value == "test"
    assert SecurityLevel.RESEARCH.value == "research"
