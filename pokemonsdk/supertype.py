"""Represents the Supertypes of cards: Pokemon, Energy, Trainer."""
from pokemonsdk import QueryBuilder


class Supertype(object):

    """Represents the Supertypes of cards: Pokemon, Energy, Trainer.

    See https://docs.pokemontcg.io/#get-all-supertypes

    Attributes:
        RESOURCE: RESTful resource
    """

    RESOURCE = 'supertypes'

    def all():
        """Get the full list of Supertypes.

        Returns:
            array: Array of Supertypes
        """
        return QueryBuilder(Supertype).array()
