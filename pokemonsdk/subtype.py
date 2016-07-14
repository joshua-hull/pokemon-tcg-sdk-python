from pokemonsdk.querybuilder import QueryBuilder


class Subtype(object):
    RESOURCE = 'subtypes'

    def all():
        return QueryBuilder(Subtype).array()
