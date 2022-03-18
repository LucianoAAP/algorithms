def study_schedule(permanence_period, target_time):
    count = 0

    try:
        for period in permanence_period:
            if period[0] <= target_time and period[1] >= target_time:
                count += 1
    except TypeError:
        return None

    return count
