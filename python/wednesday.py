from datetime import datetime, date


WEDNESDAY = 2


def time_until_wednesday():
    """
    Calculates and returns the time until the next Wednesday, in seconds
    The try/except statement handles setting the wednesday variable to the next Wednesday. An exception is raised when
    attempting to set a date that is outside of the month's range (ex. November 36th).
    """

    now = datetime.today()

    # Days until Wednesday
    days_until = (WEDNESDAY - now.weekday()) % 7

    # If today is Wednesday, look at next week's Wednesday
    if days_until == 0:
        days_until = 7

    try:
        # Update just the day
        wednesday = now.replace(day=now.day + days_until, hour=0, minute=0, second=0, microsecond=0)

    except:
        # Update day and month, and year if necessary

        updated_month = now.month + 1
        updated_year = now.year

        if updated_month == 13:
            updated_month = 1
            updated_year = now.year + 1

        # Get the days in the current month
        days_in_month = (date(updated_year, updated_month, 1) - date(now.year, now.month, 1)).days

        # The first day of next month
        first_day = now.replace(year=updated_year, month=updated_month, day=1, hour=0, minute=0, second=0,
                                microsecond=0)

        # days_until = Days remaining in current month + days until Wednesday in next month
        days_until = (days_in_month - now.day) + (WEDNESDAY - first_day.weekday()) % 7

        # Updated wednesday
        wednesday = first_day.replace(day=(first_day.day + days_until - 1))

    num_seconds = (wednesday - now).total_seconds()
    return num_seconds
