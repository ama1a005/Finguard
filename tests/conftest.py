"""Pytest configuration for FinGuard-RAG tests"""

import pytest
import sys
from pathlib import Path

# Add src directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


@pytest.fixture
def sample_query():
    """Fixture providing a sample financial compliance query"""
    return "What are the RBI capital adequacy requirements for banks?"


@pytest.fixture
def sample_jurisdiction():
    """Fixture providing sample jurisdiction"""
    return "India"


@pytest.fixture
def sample_role():
    """Fixture providing sample user role"""
    return "compliance_analyst"
