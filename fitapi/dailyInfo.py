from datetime import datetime

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
def read():
    """
    Responds to a request for /api/daily
    with the complete list of daily info

    :return:        sorted list of daily info
    """
    # Create the list of daily info from our data
    return [DAILYINFO[key] for key in sorted(DAILYINFO.keys())]