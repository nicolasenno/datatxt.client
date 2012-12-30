#!/usr/bin/env python
# encoding=utf8

# datatxt DBpedia it python integration
# test user = hacktivist

from __future__ import print_function

from requests import get

import sparql
import collections

# FIXME: ugly hack ahead, needs a virtuoso >= 6.1.6 to remove it
def unpack_row(row):
    """
    Transform row in python objects
    needed because virtuoso < 6.1.6 has a RDF/XML bug on literals
    otherwise similar to sparql.unpack_row()
    """
    pred, obj = sparql.unpack_row(row)
    if isinstance(row[1], sparql.Literal):
        try:
            str(obj)
        except UnicodeEncodeError:
            obj = obj.encode('latin1').decode('utf8')
    return pred, obj

class Datatxt(object):
    """
    Main datatxt text parsers, instantiate a class passing deviation from
    defaults globals listed above
    documentation here: https://spaziodati.3scale.net/getting-started
    """
    def __init__(self, app_key, app_id, lang, api_url, rho, epsilon, long_text, prefix, endpoint):
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

    def annotate(self, text, properties=True, wikilinks=False, rho=None):
        """ return a dictionary out of json
        """
        params = dict(self.params)
        params['text'] = text
        if rho:
            params['rho'] = rho

        r = get(self.api_url, params=self.params, headers=self.headers)
        if r.status_code == 200:
            result = r.json
            for annotation in result['annotations']:
                resource = annotation['ref'][0]['wikipedia'].replace('wikipedia.org/wiki', 'dbpedia.org/resource')
                annotation['ref'] = resource
                if properties:
                    annotation[u'properties'] = self.properties(resource, wikilinks)
            return result

    def sparql(self, query):
        # FIXME: it works only for queries with 2 columns, where the first is an IRI
        result = self.service.query(query)
        statement = query.lower()
        if 'select' in statement:
            d = collections.defaultdict(list)
            for pred, obj in (unpack_row(row) for row in result):
                d[pred].append(obj)
            return dict(d)
        elif 'ask' in statement:
            return result.hasresult()

    def properties(self, resource, wikilinks=False):
        if wikilinks:
            query = "select * where {<%s> ?pred ?obj .}" % resource
        else:
            query = "select * where { graph <%s> {<%s> ?pred ?obj .}}" % (self.prefix, resource)
        return self.sparql(query)

if __name__ == '__main__':
    print("Use datatxt-cli, this is just a python module")
