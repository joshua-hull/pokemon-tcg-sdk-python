"""Represents the Subtypes of cards."""
from pokemonsdk import QueryBuilder


class Subtype(object):

    """Represents the Subtypes of cards.

    See https://docs.pokemontcg.io/#get-all-subtypes

    Attributes:
        RESOURCE: RESTful resource
    """

    RESOURCE = 'subtypes'

    def all():
        """Get the full list of types.

        Returns:
            array: Array of types
        """
        return QueryBuilder(Subtype).array()
