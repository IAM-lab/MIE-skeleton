"""
NAME:          models.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          22/11/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Database ORM class
"""

from app import db

class PrescribingData(db.Model):
    """class for the prescription data table."""
    __tablename__ = 'practice_level_prescribing'
    id = db.Column(db.Integer, primary_key=True)
    SHA = db.Column(db.String(3))
    PCT = db.Column(db.String(3))
    practice = db.Column(db.String(6))
    BNF_code = db.Column("BNFCODE", db.String(15))
    BNF_name = db.Column("BNFNAME", db.String(40))
    items = db.Column(db.Integer)
    NIC = db.Column(db.Float)
    ACT_cost = db.Column("ACTCOST", db.Float)
    quantity = db.Column(db.Integer)

class PracticeData(db.Model):
    """Class for the practice address data table."""
    __tablename__ = 'practices'
    practice_code = db.Column(db.String(6), primary_key=True)
    practice_name = db.Column(db.Text)
    address_line_1 = db.Column(db.Text)
    address_line_2 = db.Column(db.Text)
    city = db.Column(db.Text)
    county = db.Column(db.Text)
    post_code = db.Column(db.String(10))



