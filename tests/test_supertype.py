"""Test supertype.py."""
import unittest
import vcr
from pokemonsdk import Supertype


class TestType(unittest.TestCase):

    """Test Suite for Superype."""

    def test_all_returns_supertypes(self):
        """Test Supertype.all() returns all supertypes."""
        with vcr.use_cassette('fixtures/supertypes.yaml'):
            supertypes = Supertype.all()
            self.assertEqual(["Pokémon",
                              "Energy",
                              "Trainer"], supertypes)
