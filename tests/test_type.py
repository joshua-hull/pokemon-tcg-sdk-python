"""Test type.py."""
import unittest
import vcr
from pokemonsdk import Type


class TestType(unittest.TestCase):

    """Test Suite for Type."""

    def test_all_returns_types(self):
        """Test Type.all() returns all types."""
        with vcr.use_cassette('fixtures/types.yaml'):
            types = Type.all()
            self.assertEqual(["Colorless",
                              "Dark",
                              "Darkness",
                              "Dragon",
                              "Fairy",
                              "Fighting",
                              "Fire",
                              "Grass",
                              "Lightning",
                              "Metal",
                              "Psychic",
                              "Water"], types)
