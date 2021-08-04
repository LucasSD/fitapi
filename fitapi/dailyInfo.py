from datetime import datetime

from flask import abort, make_response

date1 = datetime(1984, 1, 1).strftime("%Y-%m-%d %H:%M:%S")
date1a = datetime(1984, 1, 2).strftime("%Y-%m-%d %H:%M:%S")
date2 = datetime(1985, 1, 1).strftime("%Y-%m-%d %H:%M:%S")
date2a = datetime(1985, 1, 2).strftime("%Y-%m-%d %H:%M:%S")
date3 = datetime(1986, 1, 1).strftime("%Y-%m-%d %H:%M:%S")
date3a = datetime(1986, 1, 2).strftime("%Y-%m-%d %H:%M:%S")

# Data to serve with our API
DAILYINFO = {
    date1: {
        "startDate": date1,
        "endDate": date1a,
    },
    date2: {
        "startDate": date2,
        "endDate": date2a,
    },
    date3: {
        "startDate": date3,
        "endDate": date3a,
    },
}

# Create a handler for our read (GET) daily info
def read_all():
    """
    Responds to a request for /api/daily
    with the complete list of daily info

    :return:        sorted list of daily info
    """
    # Create the list of daily info from our data
    return [DAILYINFO[key] for key in sorted(DAILYINFO.keys())]

def read_one(startDate):
    """
    This function responds to a request for /api/daily/{startDate}
    with one matching daily event from daily info
    :param startDate:   event date
    :return:        daily event matching startDate
    """
    # Does the date exist in daily info?
    if startDate in DAILYINFO:
        day = DAILYINFO.get(startDate)

    # if not found
    else:
        abort(
            404, "Date {startDate} not found".format(startDate=startDate)
        )

    return day


def create(day):
    """
    This function creates a new daily entry in the daily info structure
    based on the payload
    :param day:  day to create in daily info structure
    :return:        201 on success, 406 if day exists already
    """
    startDate = day.get("startDate", None)
    endDate = day.get("endDate", None)

    # Does the day exist already?
    if startDate not in DAILYINFO and startDate is not None:
        DAILYINFO[startDate] = {
            "startDate": startDate,
            "endDate": endDate,
        }
        return DAILYINFO[startDate], 201

    # day already exists
    else:
        abort(
            406,
            "Date {startDate} already exists".format(startDate=startDate),
        )


def update(startDate, day):
    """
    Updates an existing daily entry in the daily info structure
    :param startDate:   date to update in the daily info structure
    :param day:  date to update
    :return:        updated daily entry
    """
    # Does the date exist in daily info?
    if startDate in DAILYINFO:
        DAILYINFO[startDate]["endDate"] = day.get("endDate")

        return DAILYINFO[startDate]

    # if does not exist
    else:
        abort(
            404, "Date {startDate} not found".format(startDate=startDate)
        )


def delete(startDate):
    """
    Deletes a date from the dailyInfo structure
    :param startDate:   date to delete
    :return:        200 on successful delete, 404 if not found
    """
    # Does the date exist?
    if startDate in DAILYINFO:
        del DAILYINFO[startDate]
        return make_response(
            "{startDate} successfully deleted".format(startDate=startDate), 200
        )

    # date not found
    else:
        abort(
            404, "Date {startDate} not found".format(startDate=startDate)
        )
