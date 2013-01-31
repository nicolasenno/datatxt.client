#!/usr/bin/env python
# encoding=utf8
from logging import getLogger
from requests import get
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface
import collections
import sparql

DatatxtMessageFactory = MessageFactory(u'datatxt.client')
logger = getLogger('datatxt.client')


class Layer(Interface):
    """Layer Marker"""

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

class Datatxt():
    """
    Main datatxt text parsers, instantiate a class passing deviation from
    defaults globals listed above
    documentation here: https://spaziodati.3scale.net/getting-started
    """
    def __init__(self, app_key,
                 app_id,
                 lang,
                 api_url,
                 rho,
                 epsilon,
                 long_text,
                 prefix,
                 endpoint):

        self.api_url = api_url
        self.params = {
            'app_key' : app_key,
            'app_id' : app_id,
            'lang': lang,
            'dbpedia' : 'false',
            'rho' : rho,
            'epsilon' : epsilon,
            'long_text' : long_text,
        }
        self.headers = {
            'Accept' : 'application/json'
        }
        self.default_rho = rho
        self.service = sparql.Service(endpoint)
        self.prefix = prefix

    @property
    def settings_interface(self):
        return "datatxt.client.interfaces.IDatatxtSettings"

    def tags(self, text):
        """ return a list of tags
        """
        self.params['text'] = text

        res = get(self.api_url, params=self.params, headers=self.headers)
        if res.status_code == 200:
            result = res.json()
            return [annotation['title'] for annotation in result['annotations']]

