from setuptools import setup, find_packages
import os, sys

PACKAGE_NAME = "testmill"
PACKAGE_VERSION = "1.0.0"

SUMMARY = 'Testmill Test Management Server'

DESCRIPTION = """Tool for Managing Test Cases and interoperate with many resources."""

dependencies =  ['django',
                 'pygments',
                 'feedparser',
                 'couchdb'
                 ]

setup(name=PACKAGE_NAME,
      version=PACKAGE_VERSION,
      description=SUMMARY,
      long_description=DESCRIPTION,
      author='Adam Christian',
      author_email='adam.christian@gmail.com',
      url='http://admc.github.com/testmill/',
      include_package_data = True,
      packages = find_packages(exclude=['test', 'scripts']),
      package_data = {'': ['*.js', '*.css', '*.html', '*.txt', '*.py' ],},
      platforms =['Any'],
      install_requires = dependencies,
      classifiers=['Development Status :: 2 - Pre-Alpha',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: Apache Software License',
                   'Operating System :: OS Independent',
                   'Topic :: Software Development',
                  ],
     )

