import os
from datetime import datetime

from __init__ import db
from models import Daily, User

# Data to initialize database with
DAILYINFO = [
    {
        "fname": "Lucas",
        "lname": "Stone-Drake",
        "dates": [
            (datetime(1984, 1, 2), datetime(1984, 1, 1)),
            (datetime(1985, 1, 2), datetime(1985, 1, 1)),
            (datetime(1986, 1, 2), datetime(1986, 1, 1)),
        ],
    },
    {
        "fname": "John",
        "lname": "Smith",
        "dates": [
            (datetime(2000, 1, 2), datetime(2000, 1, 1)),
            (datetime(2001, 1, 2), datetime(2001, 1, 1)),
            (datetime(2002, 1, 2), datetime(2001, 1, 1)),
        ],
    },
]

# Delete database file if it exists currently
if os.path.exists("daily.db"):
    os.remove("daily.db")

# Create the database
db.create_all()

# Iterate over the DAILYINFO structure and populate the database
for user in DAILYINFO:
    u = User(lname=user.get("lname"), fname=user.get("fname"))
    # Add the dates for the person
    for date in user.get("dates"):
        endDate, startDate = date
        u.dates.append(
            Daily(
                endDate=endDate,
                startDate=startDate,
            )
        )
    db.session.add(u)

db.session.commit()
