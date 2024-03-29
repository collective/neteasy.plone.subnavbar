from setuptools import setup, find_packages
import os

version = '1.1a1'

setup(name='neteasy.plone.subnavbar',
      version=version,
      description="This product will provide a second level navbar for Plone sites.",
      long_description=open("README.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='navigation plone ',
      author='Jim Nelson',
      author_email='neteasy@medialog.no',
      url='https://github.com/collective/neteasy.plone.subnavbar/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['neteasy'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
