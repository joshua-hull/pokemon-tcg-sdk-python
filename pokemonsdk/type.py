from pokemonsdk.querybuilder import QueryBuilder


class Type(object):

    """Represents the types of Pokemon: Water, Grass, Fire, etc.

    See https://docs.pokemontcg.io/#card-types

    Attributes:
        RESOURCE: RESTful resource
    """

    RESOURCE = 'types'

    def all():
        """Get the full list of types.

        Returns:
            array: Array of types
        """
        return QueryBuilder(Type).array()
