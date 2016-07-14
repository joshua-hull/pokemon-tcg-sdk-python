from pokemonsdk.querybuilder import QueryBuilder


class Subtype(object):
    RESOURCE = 'subtypes'

    def all(self):
        return QueryBuilder(Subtype).array()
