"""Test card.py."""
import unittest
import vcr
from pokemonsdk import Card


class TestCard(unittest.TestCase):

    """Test card.py."""

    def test_find_returns_card(self):
        """Testing Card.find() returns a card."""
        with vcr.use_cassette('fixtures/Gardevoir.yaml'):
            card = Card.find('xy7-54')

            self.assertEqual('xy7-54', card.id)
            self.assertEqual('Gardevoir', card.name)
            self.assertEqual('https://s3.amazonaws.com/pokemontcg/xy7/54.png',
                             card.image_url)
            self.assertEqual('Stage 2', card.subtype)
            self.assertEqual('Pokémon', card.supertype)
            self.assertEqual({'name': 'Bright Heal',
                              'text': 'Once during your turn '
                                      '(before your attack), '
                                      'you may heal 20 damage '
                                      'from each of your Pokémon.'},
                             card.ability)
            self.assertEqual('130', card.hp)
            self.assertEqual(['Colorless', 'Colorless'], card.retreat_cost)
            self.assertEqual('54', card.number)
            self.assertEqual('TOKIYA', card.artist)
            self.assertEqual('Rare Holo', card.rarity)
            self.assertEqual('XY', card.series)
            self.assertEqual('Ancient Origins', card.set)
            self.assertEqual('xy7', card.set_code)
            self.assertEqual(['Fairy'], card.types)
            self.assertEqual(1, len(card.attacks))
            self.assertEqual(3, len(card.attacks[0]['cost']))
            self.assertEqual('Telekinesis', card.attacks[0]['name'])
            self.assertEqual('', card.attacks[0]['damage'])
            self.assertEqual(3, card.attacks[0]['convertedEnergyCost'])
            self.assertEqual([{'type': 'Metal', 'value': '\xd72'}],
                             card.weaknesses)
            self.assertEqual([{'type': 'Darkness', 'value': '-20'}],
                             card.resistances)

    def test_all_with_params_return_cards(self):
        """Testing Card.where() returns cards."""
        with vcr.use_cassette('fixtures/metal_psychic.yaml'):
            cards = Card.where(types='metal,psychic') \
                        .all()

            self.assertEqual(5, len(cards))

    def test_all_with_page_returns_cards(self):
        """Testing Card.where() with a page returns that page."""
        with vcr.use_cassette('fixtures/all_first_page.yaml'):
            cards = Card.where(page=1).all()

            self.assertEqual(100, len(cards))

    def test_all_with_page_and_page_size_returns_card(self):
        """Testing Card.where().

        Testing Card.where with a page and size returns that page with that
        many results.
        """
        with vcr.use_cassette('fixtures/all_first_page_one_card.yaml'):
            cards = Card.where(page=1).where(pageSize=1).all()

            self.assertEqual(1, len(cards))
