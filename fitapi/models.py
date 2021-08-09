from datetime import datetime

from marshmallow import fields

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


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sqla_session = db.session

    dates = fields.Nested("UserDailySchema", default=[], many=True)


class UserDailySchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """
    user_id = fields.Int()
    startDate = fields.Str()
    endDate = fields.Str()


class DailySchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Daily
        sqla_session = db.session

    user = fields.Nested("DailyUserSchema", default=None)


class DailyUserSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """

    user_id = fields.Int()
    lname = fields.Str()
    fname = fields.Str()
    
