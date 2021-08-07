from datetime import datetime
from fitapi import db, ma

class Daily(db.Model):
    __tablename__ = 'daily'
    day_id = db.Column(db.Integer,)
    startDate = db.Column(db.DateTime, primary_key=True, index=True)
    endDate = db.Column(db.DateTime)

class DailySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Daily
        sqla_session = db.session 