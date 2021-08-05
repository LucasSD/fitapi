from datetime import datetime
from config import db, ma

class Daily(db.Model):
    __tablename__ = 'daily'
    day_id = db.Column(db.Integer, primary_key=True)
    startDate = db.Column(db.DateTime, index=True)
    endDate = db.Column(db.DateTime)

class DailySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Daily
        sqla_session = db.session 