from setuptools import setup, find_packages
import os

version = '1.0.0rc1'

setup(name='atreal.richfile.image',
      version=version,
      description="Image Support Plugin for RichFileQualifier",
      long_description=open("README.txt").read() + "\n",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone richfile atreal image',
      author='atReal',
      author_email='contact@atreal.net',
      url='http://www.atreal.net/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['atreal', 'atreal.richfile'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'atreal.richfile.qualifier',
          'atreal.filestorage.common',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
