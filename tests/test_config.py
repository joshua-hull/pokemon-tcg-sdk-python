"""Test config.py."""
import unittest
from pokemonsdk import __endpoint__


class TestConfig(unittest.TestCase):

    """Test config.py."""

    def test_has_proper_endpoint(self):
        """Test API endpoint is correct."""
        self.assertEqual('https://api.pokemontcg.io/v1', __endpoint__)
