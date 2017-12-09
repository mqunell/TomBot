from datetime import datetime, date


def time_until(input_weekday):
    """ Return seconds as integer

    Calculates and returns the time until the next target weekday, in seconds
    The try/except statement handles setting the target variable to the next target weekday. An exception is raised when
    attempting to set a date that is outside of the month's range (ex. November 36th).
    """

    # The current datetime
    now = datetime.today()

    # Testing - makes "now" a different day
    now = now.replace(month=12, day=5)

    # Get the value of the target weekday
    target_weekday_num = input_weekday.value

    # Days until target
    days_until = (target_weekday_num - now.weekday()) % 7

    # If today is input_weekday, look at next week's input_weekday
    if days_until == 0:
        days_until = 7

    try:
        # Leave month/year alone; update day; set hour/minute/second/microsecond to 0
        target_weekday = now.replace(day=now.day + days_until, hour=0, minute=0, second=0, microsecond=0)

    except:
        # Update day and month, and year if necessary
        updated_month = now.month + 1
        updated_year = now.year

        if updated_month == 13:
            updated_month = 1
            updated_year = now.year + 1

        # Get the days in the current month
        days_in_month = (date(updated_year, updated_month, 1) - date(now.year, now.month, 1)).days

        # The date of the next input_weekday
        target_date = days_until - (days_in_month - now.day)

        # Target weekday
        target_weekday = datetime(year=updated_year, month=updated_month, day=target_date, hour=0, minute=0, second=0,
                                  microsecond=0)

    # Seconds between now and target_weekday
    num_seconds = (target_weekday - now).total_seconds()

    # Test output - prints the current day, next input_weekday, and number of days until then
    print("Now: %s" % str(now))
    weekday_strings = {0: "Mon", 1: "Tues", 2: "Wed", 3: "Thurs", 4: "Fri", 5: "Sat", 6: "Sun"}
    print("%s: %s" % (weekday_strings[target_weekday_num], str(target_weekday)))
    print("Approx. days until %s: %f" % (weekday_strings[target_weekday_num], (num_seconds / 60.0 / 60.0 / 24.0)))

    return num_seconds
