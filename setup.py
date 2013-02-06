#!/usr/bin/env python
from setuptools import setup, find_packages
import sys, os

version = '0.1.0'
shortdesc = "python interface for SpazioDati's dataTXT and DBpedia"
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
tests_require = ['interlude']

setup(name='datatxt.client',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers = [
            'Development Status :: 2 - Pre-Alpha',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: POSIX',
            'Natural Language :: Italian',
            'Natural Language :: English',
            'Programming Language :: Python',
            'Topic :: Database',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Text Processing :: Indexing'
      ],
      keywords='',
      author='',
      author_email='',
      url=u'',
      license='Python Software Foundation License',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['datatxt'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
            'sparql-client >= 0.13',
            'requests >= 0.11'
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
