def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    count = 0

    for period in permanence_period:
        if (type(period) != tuple
                or type(period[0]) != int or type(period[1]) != int):
            return None
        if period[0] <= target_time and period[1] >= target_time:
            count += 1

    return count
