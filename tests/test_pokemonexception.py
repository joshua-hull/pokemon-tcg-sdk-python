"""Test restclient.py PokemonException."""
import unittest
from pokemonsdk import PokemonException


class TestPokemonException(unittest.TestCase):

    """Test PokemonException."""

    def test_constructor_sets_description(self):
        """Test PokemonException description is set correctly."""
        description = "An error has occured"
        exception = PokemonException(description)

        self.assertEqual(description, exception.__str__())
