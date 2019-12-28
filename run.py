"""
NAME:          run.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          03/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   File that runs the Flask application (local hosting). To run the app, run this file
               e.g. python run.py
               Open an internet browser and enter the following URL:
               http://127.0.0.1:5000/dashboard/home/
"""

from app import app
app.run()
