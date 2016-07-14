from pokemonsdk.querybuilder import QueryBuilder


class Supertype(object):
    RESOURCE = 'supertypes'

    def all():
        return QueryBuilder(Supertype).array()
