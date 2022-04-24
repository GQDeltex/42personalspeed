def days_to_workhours(days: int):
    neg = False
    if days < 0:
        days *= -1
        neg = True
    workdays = min(5, (days % 7))
    days -= days % 7
    workdays += round((days / 7) * 5)
    if neg:
        workdays *= -1
    return workdays * 8


def workhours_to_days(workhours: int):
    if workhours == 0:
        return 0
    workdays = round(workhours / 8)
    weekends = int(workdays / 5)
    if (workhours % 40 <= 3):
        weekends -= 1
    days = workdays + (2 * weekends)
    return days
