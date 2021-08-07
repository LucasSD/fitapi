import os
from datetime import datetime

from config import db
from models import Daily

# Data to initialize database with
DAILYINFO = [
    {'endDate': datetime(1984, 1, 2), 'startDate': datetime(1984, 1, 1)},
    {'endDate': datetime(1985, 1, 2), 'startDate': datetime(1985, 1, 1)},
    {'endDate': datetime(1986, 1, 2),'startDate': datetime(1986, 1, 1)}
]

# Delete database file if it exists currently
if os.path.exists('daily.db'):
    os.remove('daily.db')

# Create the database
db.create_all()

# Iterate over the DAILYINFO structure and populate the database
for daily in DAILYINFO:
    d = Daily(startDate=daily['startDate'], endDate=daily['endDate'])
    db.session.add(d)

db.session.commit()
