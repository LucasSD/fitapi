from datetime import datetime

from flask import abort, make_response

from fitapi import db
from fitapi.models import Daily, DailySchema

# Create a handler for our read (GET) daily info
def read_all():
    """
    Responds to a request for /api/daily
    with the complete list of daily info

    :return:        json string of list of daily info
    """
    # Create the list of daily info from our data
    daily = Daily.query.order_by(Daily.startDate).all()

    # Serialize the data for the response
    daily_schema = DailySchema(many=True)
    return daily_schema.dump(daily)


def read_one(startDate):
    """
    This function responds to a request for /api/daily/{startDate}
    with one matching daily event from daily info
    :param startDate:   event date
    :return:        daily event matching startDate
    """

    d, m, y = (int(x) for x in startDate.split("-"))
    query_date = datetime(y, m, d)

    # Get the date requested
    day = Daily.query.filter(Daily.startDate == query_date).one_or_none()

    # Does the date exist in daily info?
    if day is not None:

        # Serialize the data for the response
        day_schema = DailySchema()
        return day_schema.dump(day)

    # if not found
    else:
        abort(404, "Date {startDate} not found".format(startDate=startDate))


def create(day):
    """
    This function creates a new daily entry in the daily info structure
    based on the payload
    :param day:  day to create in daily info structure
    :return:        201 on success, 406 if day exists already
    """
    startDate = day.get("startDate")
    d, m, y = (x for x in startDate.split("-"))
    d = d[0:2].lstrip("0")
    query_date = datetime(int(y), int(m), int(d))

    existing_day = Daily.query.filter(Daily.startDate == query_date).one_or_none()

    # Can we insert this day?
    if existing_day is None:
        day["startDate"] = query_date

        # Create a daily instance using the schema and the passed-in day
        schema = DailySchema()
        new_day = schema.load(day, session=db.session)

        # Add the day to the database
        db.session.add(new_day)
        db.session.commit()

        # Serialize and return the newly created day in the response
        return schema.dump(new_day), 201

    # Otherwise, nope, day exists already
    else:
        abort(409, f"Date {startDate} exists already")


def update(startDate, day):
    """
    Updates an existing day in the daily info structure
    Throws an error if a day with the date we want to update to
    already exists in the database.
    :param startDate:   startDate of the day to update in the daily info structure
    :param day:      day to update
    :return:            updated day structure
    """
    # Get the day requested from the db into session
    update_day = Daily.query.filter(Daily.startDate == startDate).one_or_none()

    # Try to find an existing day with the same date as the update
    endDate = day.get("endDate")
    startDate = day.get("startDate")

    existing_day = (
        Daily.query.filter(Daily.endDate == endDate)
        .filter(Daily.startDate == startDate)
        .one_or_none()
    )

    # If day does not exist
    if update_day is None:
        abort(
            404,
            "Date {startDate} not found".format(startDate=startDate),
        )

    # Date already exists
    elif existing_day is not None and existing_day.startDate != startDate:
        abort(
            409,
            "Entry {endDate} {startDate} exists already".format(
                endDate=endDate, startDate=startDate
            ),
        )

    else:

        # turn the payload into a db object
        schema = DailySchema()
        update = schema.load(day, session=db.session)

        # Set the startDate to the day we want to update
        update.startDate = update_day.startDate

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated day in the response
        data = schema.dump(update_day)

        return data, 200


def delete(startDate):
    """
    Deletes a day from the daily info structure
    :param startDate:   startDate of the day to delete
    :return:            200 on successful delete, 404 if not found
    """

    d, m, y = (int(x) for x in startDate.split("-"))
    query_date = datetime(y, m, d)

    # Get the day requested
    day = Daily.query.filter(Daily.startDate == query_date).one_or_none()

    # Day exists?
    if day is not None:
        db.session.delete(day)
        db.session.commit()
        return make_response(
            "Date {startDate} deleted".format(startDate=startDate), 200
        )

    # Day does not exist
    else:
        abort(
            404,
            "Date {startDate} not found".format(startDate=startDate),
        )
