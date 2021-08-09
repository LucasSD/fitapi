from datetime import datetime

from flask import abort, make_response

from fitapi import db
from fitapi.models import Daily, DailySchema, User


def read_all():
    """
    Responds to a request for /api/daily/dates
    with the complete list of dates
    :return:                json list of all dates for all people
    """
    dates = Daily.query.order_by(db.desc(Daily.startDate)).all()

    # Serialize the list of notes from our data
    date_schema = DailySchema(many=True) # can exclude fields here if desired
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

    d, m, y = (int(x) for x in startDate.split("-"))
    query_date = datetime(y, m, d)

    # Query the database for the date
    date = (
        Daily.query.join(User, User.user_id == Daily.user_id)
        .filter(User.user_id == user_id)
        .filter(Daily.startDate == query_date)
        .one_or_none()
    )

    # Date exists
    if date is not None:
        date_schema = DailySchema()
        data = date_schema.dump(date)
        return data

    # Date does not exist
    else:
        abort(404, f"Date: {startDate} not found")


