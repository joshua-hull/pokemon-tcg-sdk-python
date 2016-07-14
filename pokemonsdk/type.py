from pokemonsdk.querybuilder import QueryBuilder


class Type(object):
    RESOURCE = 'types'

    def all():
        return QueryBuilder(Type).array()
