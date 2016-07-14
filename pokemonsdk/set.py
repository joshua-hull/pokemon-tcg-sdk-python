import json
from pokemonsdk.querybuilder import QueryBuilder
from pokemonsdk.config import __endpoint__


class Set(object):
    
    """Represents the Sets of cards.

    See https://docs.pokemontcg.io/#get-all-sets

    Attributes:
        RESOURCE: RESTful resource
    """

    RESOURCE = 'sets'

    def __init__(self, response_dict={}):
        """Initalizes instance with given response_dict.

        Args:
            response_dict (dictionary): The response from the API

        Returns:
            object: Set instance
        """
        self.code = response_dict.get('code')
        self.name = response_dict.get('name')
        self.series = response_dict.get('series')
        self.total_cards = response_dict.get('totalCards')
        self.standard_legal = response_dict.get('standardLegal')
        self.release_date = response_dict.get('releaseDate')

    def where(**kwargs):
        """Get a filtered list of types.

        Returns:
            object: QueryBuilder instance
        """
        return QueryBuilder(Set).where(**kwargs)

    def all():
        """Get the full list of sets.

        Returns:
            array: Array of sets
        """
        return QueryBuilder(Set).all()
