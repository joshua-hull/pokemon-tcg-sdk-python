from pokemonsdk.querybuilder import QueryBuilder


class Supertype(object):
    RESOURCE = 'supertypes'

    def all(self):
        return QueryBuilder(Supertype).array()
