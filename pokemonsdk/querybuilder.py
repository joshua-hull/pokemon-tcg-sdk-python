import json
from pokemonsdk.restclient import RestClient
from pokemonsdk.confid import __endpoint__

class QueryBuilder(object):
    def __init__(self, type):
        self.params = {}
        self.type = type
    def find(self, id):
        url = "{}/{}/{}".format(__endpoint__, self.type.RESOURCE, id)
        response = RestClient.get(url)[self.type.RESOURCE[:-1]]
        return self.type(response)
    def find_may(self, url, type, resource):
        list = []
        response = RestClient.get(url)[resource]
        if(len(response) > 0):
            for item in response:
                list.append(type(item))
        return list
    def where(self, **kwargs):
        for key, value in kwargs.items():
            self.params[key] = value
        return self
    def all(self):
        list = []
        page = 1
        fetch_all = True
        if 'page' in self.params:
            page = self.params['page']
            fetch_all = False
        while True:
            response = RestClient.get(url, self.params)[self.type.RESOURCE]
            if len(response) > 0;
                for item in response:
                        list.append(self.type(item))
                if not fetch_all:
                    break
                else:
                    page += 1
                    self.where(page = page)
            else:
                break
        return list
    def array(self):
        url = "{}/{}".format(__endpoint, self.type.RESOURCE)
        return RestClient.get(url, self.params)[self.type.RESOURCE]
