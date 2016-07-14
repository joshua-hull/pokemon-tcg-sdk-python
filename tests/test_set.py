"""Test set.py."""
import unittest
import vcr
from pokemonsdk import Set


class TestType(unittest.TestCase):

    """Test Suite for Set."""

    def test_find_returns_set(self):
        """Test Set.find() returns a set."""
        with vcr.use_cassette('fixture/xy1.yaml'):
            set = Set.find('xy1')

            self.assertEqual('xy1', set.code)
            self.assertEqual('XY', set.name)
            self.assertEqual('XY', set.series)
            self.assertEqual(140, set.total_cards)
            self.assertEqual(True, set.standard_legal)
            self.assertEqual('02/05/2014', set.release_date)

    def test_where_filters_on_name(self):
        """Test Set.where() returns a set."""
        with vcr.use_cassette('fixture/filtered_sets.yaml'):
            sets = Set.where(name='jungle').all()

            self.assertEqual(1, len(sets))
            self.assertEqual('base2', sets[0].code)

    def test_all_returns_all_sets(self):
        """Test Set.all() returns all sets."""
        with vcr.use_cassette('fixture/all_sets.yaml'):
            sets = Set.all()

            self.assertGreater(len(sets), 25)
