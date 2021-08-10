from datetime import datetime

from flask import abort, make_response

from fitapi import db
from fitapi.models import Daily, DailySchema, User, UserSchema


def read_all():
    """
    This function responds to a request for /api/daily
    with the complete lists of users
    :return:        json string of list of users
    """
    users = User.query.order_by(User.lname).all()

    # Serialize the data for the response
    user_schema = UserSchema(many=True)
    data = user_schema.dump(users)
    return data


def read_one(user_id):
    """
    This function responds to a request for /api/daily/{user_id}
    with one matching user from users
    :param user_id:   Id of user to find
    :return:            user matching id
    """
    # Build the initial query
    user = (
        User.query.filter(User.user_id == user_id)
        .outerjoin(Daily)
        .one_or_none()
    )

    # User exists?
    if user is not None:

        # Serialize the data for the response
        user_schema = UserSchema()
        data = user_schema.dump(user)
        return data

    # user not present
    else:
        abort(404, f"User Id: {user_id} not found")



