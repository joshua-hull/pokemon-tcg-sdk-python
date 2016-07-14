import json
from pokemonsdk.querybuilder import QueryBuilder
from pokemonsdk.config import __endpoint__


class Set(object):
    RESOURCE = 'sets'

    def __init__(self, response_dict={}):
        self.code = response_dict.get('code')
        self.name = response_dict.get('name')
        self.series = response_dict.get('series')
        self.total_cards = response_dict.get('totalCards')
        self.standard_legal = response_dict.get('standardLegal')
        self.release_date = response_dict.get('releaseDate')

    def where(**kwargs):
        return QueryBuilder(Set).where(**kwargs)

    def all():
        return QueryBuilder(Set).all()
