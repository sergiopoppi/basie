#!/usr/bin/env python
#coding=utf-8
from distutils.core import setup

setup(
      name = "basie",
      version = "0.6.5",
      description = "schedule creator for italian radiotelescopes",
      author = "Marco Bartolini, Simona Righini",
      author_email = "bartolini@ira.inaf.it",
      maintainer = "Marco Bartolini",
      license = "License :: OSI Approved :: BSD License",
      url = "http://github.com/flyingfrog81/basie/",
      packages = ["basie", "basie.scanmode"],
      package_dir = {"basie" : "src", "basie.scanmode" : "src/scanmode"},
      package_data = {"basie" : ["schemas/*.ini",
                                 "user_templates/*.txt"]},
      scripts = ["scripts/basie"],
     )
