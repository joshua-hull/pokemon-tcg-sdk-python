import json
from pokemonsdk.querybuilder import QueryBuilder


class Card(object):

    """Represents a card.

    See https://docs.pokemontcg.io/#cards

    Attributes:
        RESOURCE: RESTful resource
    """

    RESOURCE = 'cards'

    def __init__(self, response_dict={}):
        """Initalize instance with given response_dict.

        Args:
            response_dict (dictionary): The response from the API

        Returns:
            object: Card instance
        """
        self.id = response_dict.get('id')
        self.name = response_dict.get('name')
        self.image_url = response_dict.get('imageUrl')
        self.subtype = response_dict.get('subtype')
        self.supertype = response_dict.get('supertype')
        self.ability = response_dict.get('ability')
        self.hp = response_dict.get('hp')
        self.retreat_cost = response_dict.get('retreatCost')
        self.number = response_dict.get('number')
        self.artist = response_dict.get('artist')
        self.rarity = response_dict.get('rarity')
        self.series = response_dict.get('series')
        self.set = response_dict.get('set')
        self.set_code = response_dict.get('setCode')
        self.types = response_dict.get('types')
        self.attacks = response_dict.get('attacks')
        self.weaknesses = response_dict.get('weaknesses')
        self.resistances = response_dict.get('resistances')

    def find(id):
        """Return a specific Card given an id.

        Args:
            id (string): The Card id

        Returns:
            object: Card instance
        """
        return QueryBuilder(Card).find(id)

    def where(**kwargs):
        """Get filtered list of cards.

        Returns:
            object: QueryBuilder instance
        """
        return QueryBuilder(Card).where(**kwargs)

    def all():
        """Get the full list of Cards.

        Returns:
            array: Array of Cards
        """
        return QueryBuilder(Card).all()
