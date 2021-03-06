************************************************************
Python library to leverage SpazioDati's dataTXT with DBpedia
************************************************************

`datatxt` is a library to query a dataTXT service and to enrich annotations
with queries to DBpedia SPARQL endpoint. It will automatically
convert literals to the corresponding Python types.

Visit http://spaziodati.eu/dataTXT for documentation and
examples.


API
---

First you instantiate a dataTXT class::

    d = datatxt.Datatxt()

Then you ask for annotation::

    result = d.annotation(text)

You will receive a dictionary with annotation as DBpedia resources and for
each resource you will receive all properties found in the DBpedia triplestore.

The library will automatically convert typed literals to a coresponding
simple type in Python. Dates are also converted if the dateutil_ library is
available.

.. _dateutil: http://labix.org/python-dateutil

License
-------
This software is licensed under BSD license, included as LICENSE.txt in the
source distribution.