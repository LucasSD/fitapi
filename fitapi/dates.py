from flask import make_response, abort
from fitapi import db
from fitapi.models import User, Daily, DailySchema

def read_all():
    """
    Responds to a request for /api/daily/dates
    with the complete list of dates
    :return:                json list of all dates for all people
    """
    dates = Daily.query.order_by(db.desc(Daily.startDate)).all()

    # Serialize the list of notes from our data
    date_schema = DailySchema(many=True, exclude=["user.dates"])
    data = date_schema.dump(dates)
    return data

def read_one(user_id, startDate):
    """
    Responds to a request for
    /api/daily/{user_id}/dates/{startDate}
    with one matching date for the associated user
    :param user_id:       Id of user the date is related to
    :param startDate:     startDate
    :return:                json string of date contents
    """
    # Query the database for the date
    date = (
        Daily.query.join(User, User.user_id == Daily.user_id)
        .filter(User.user_id == user_id)
        .filter(Daily.startDate == startDate)
        .one_or_none()
    )

    # Date exists
    if date is not None:
        note_schema = DailySchema()
        data = note_schema.dump(date)
        return data

    # Date does not exist
    else:
        abort(404, f"Date: {startDate} not found")


