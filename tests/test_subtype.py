"""Test subtype.py."""
import unittest
import vcr
from pokemonsdk import Subtype


class TestType(unittest.TestCase):

    """Test Suite for Superype."""

    def test_all_returns_subtypes(self):
        """Test Subtype.all() returns all subtypes."""
        with vcr.use_cassette('fixtures/subtypes.yaml'):
            subtypes = Subtype.all()
            self.assertTrue(len(subtypes) == 17)
            self.assertTrue('Basic' in subtypes)
            self.assertTrue('Stage 1' in subtypes)
            self.assertTrue('Stage 2' in subtypes)
