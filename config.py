"""
NAME:          config.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          03/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Configuration file, contains details to setup Flask app i.e. path to database file
"""

import os

DEBUG = True
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'abxdb.db')
DATABASE_CONNECT_OPTIONS = {}
THREADS_PER_PAGE = 2
CSRF_ENABLED = True
CSRF_SESSION_KEY = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"
SECRET_KEY = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"