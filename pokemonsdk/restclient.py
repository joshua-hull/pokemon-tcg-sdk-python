"""Handles make HTTP REST calls."""
import json
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from urllib.parse import urlencode


class RestClient(object):
    def get(url, params={}):
        request_url = url
        if len(params) > 0:
            request_url = "{}?{}".format(url, urlencode(params))
        try:
            req = Request(request_url, headers={'User-Agent': 'Mozilla 5.0'})
            response = json.loads(urlopen(req).read().decode("utf-8"))
            return response
        except HTTPError as err:
            raise PokemonException(err.read())


class PokemonException(Exception):
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description
