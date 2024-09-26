from .. import db
from datetime import datetime

class Task(db.Model):
    __tablename__ = 'dummy_table'

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False)
    Title__c = db.Column(db.String(100), nullable=False)
    CreatedAt = db.Column(db.DateTime, default=datetime.now())

    def to_dict(self):
        return {
            'Id': self.Id,
            'Name': self.Name,
            'Title': self.Title__c,
            'CreatedAt': self.CreatedAt
        }