"""Module to query different resources of the API."""

import json
from pokemonsdk.restclient import RestClient
from pokemonsdk.config import __endpoint__


class QueryBuilder(object):

    """Common queries for the different resouces."""

    def __init__(self, type):
        """Initalize instance with given response_dict.

        Args:
            type (object): The resource type being queried

        Returns:
            object: QueryBuilder instance
        """
        self.params = {}
        self.type = type

    def find(self, id):
        """Find a specific instance of a resource given an id.

        Args:
            id (string): The resource id being queried

        Returns:
            object: QueryBuilder instance
        """
        url = "{}/{}/{}".format(__endpoint__, self.type.RESOURCE, id)
        response = RestClient.get(url)[self.type.RESOURCE[:-1]]
        return self.type(response)

    def find_may(self, url, type, resource):
        """Find a list of resouces.

        Args:
            url (string): The url to query
            type (object): The resource type we're querying
            resource (string): The RESTful resource to query

        Returns:
            object: List of resources
        """
        list = []
        response = RestClient.get(url)[resource]
        if len(response) > 0:
            for item in response:
                list.append(type(item))
        return list

    def where(self, **kwargs):
        """Get a filtered list of a resource.

        Returns:
            object: QueryBuilder instance
        """
        for key, value in kwargs.items():
            self.params[key] = value
        return self

    def all(self):
        """Get the full list of resources.

        Returns:
            array: Array of resources
        """
        list = []
        page = 1
        fetch_all = True
        url = "{}/{}".format(__endpoint__, self.type.RESOURCE)
        if 'page' in self.params:
            page = self.params['page']
            fetch_all = False
        while True:
            response = RestClient.get(url, self.params)[self.type.RESOURCE]
            if len(response) > 0:
                for item in response:
                    list.append(self.type(item))
                if not fetch_all:
                    break
                else:
                    page += 1
                    self.where(page=page)
            else:
                break
        return list

    def array(self):
        """Get an array of resources.

        Returns:
            array: Array of resources
        """
        url = "{}/{}".format(__endpoint__, self.type.RESOURCE)
        return RestClient.get(url, self.params)[self.type.RESOURCE]
