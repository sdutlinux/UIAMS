#-*- coding: UTF-8 -*-

from app import db

class Major(db.Model):

    '''学院专业表，字段包括：
    专业名称，专业所在学院'''

    __tablename__ = 'major'
    id = db.Column(db.Integer, primary_key=True)
    major_id = db.Column(db.String(128), unique = True)
    major_name = db.Column(db.String(128))
    id_acachemy = db.Column(db.Integer, db.ForeignKey('unit.id'))

    def to_json(self):
        return {
            'id': self.major_id,
            'major_name': self.major_name
        }

    def __init__(self, major_id, major_name):
        self.major_id = major_id
        self.major_name = major_name

    def __repr__(self):
        return '<Major %r>' % self.major_name
