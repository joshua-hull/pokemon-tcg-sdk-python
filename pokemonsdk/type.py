from pokemonsdk.querybuilder import QueryBuilder


class Type(object):
    RESOURCE = 'types'

    def add(self):
        return QueryBuilder(Type).array()
