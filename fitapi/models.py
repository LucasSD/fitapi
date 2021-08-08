from datetime import datetime
from fitapi import db, ma


class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32))
    fname = db.Column(db.String(32))
    dates = db.relationship(
        "Daily",
        backref="user",
        cascade="all, delete, delete-orphan",
        single_parent=True,
        order_by="desc(Daily.startDate)",
    )


class Daily(db.Model):
    __tablename__ = "daily"
    startDate = db.Column(db.DateTime, primary_key=True, index=True)
    endDate = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))


class DailySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Daily
        sqla_session = db.session
