from datetime import datetime, date


def time_until(input_weekday):
    """
    Calculates and returns the time until the next target weekday, in seconds
    The try/except statement handles setting the target variable to the next target weekday. An exception is raised when
    attempting to set a date that is outside of the month's range (ex. November 36th).
    """

    # The current daytime
    now = datetime.today()

    # Testing - makes "now" a different day
    #now = now.replace(month=11, day=23)

    # Get the value of the target weekday
    target_weekday_num = input_weekday.value

    # Days until target
    days_until = (target_weekday_num - now.weekday()) % 7

    # If today is w, look at next week's w
    if days_until == 0:
        days_until = 7

    try:
        # Update just the day
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

        # The first day of next month
        first_day = now.replace(year=updated_year, month=updated_month, day=1, hour=0, minute=0, second=0,
                                microsecond=0)

        # days_until = Days remaining in current month + days until w in next month
        days_until = (days_in_month - now.day) + (target_weekday_num - first_day.weekday()) % 7

        if updated_month != now.month:
            days_until += 1

        # Updated target
        target_weekday = first_day.replace(day=(first_day.day + days_until - 1))

    num_seconds = (target_weekday - now).total_seconds()

    # Test output - prints the current day, next target, and number of days until Wednesday
    print("Now: %s" % str(now))
    weekday_strings = {0: "Mon", 1: "Tues", 2: "Wed", 3: "Thurs", 4: "Fri", 5: "Sat", 6: "Sun"}
    print("%s: %s" % (weekday_strings[target_weekday_num], str(target_weekday)))
    print("Approx. days until %s: %f" % (weekday_strings[target_weekday_num], (num_seconds / 60.0 / 60.0 / 24.0)))

    return num_seconds
