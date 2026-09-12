from datetime import date


def month_index(value):
    """
    Converts a date into a comparable month index.
    """

    return value.year * 12 + value.month


def resolve_end_date(end_date, current_date):
    """
    Resolves an open-ended employment period.
    """

    if end_date is None:
        return date(current_date.year, current_date.month, 1)

    return end_date


def merge_experience_periods(periods, current_date):
    """
    Merges overlapping or continuous employment periods.
    """

    resolved_periods = []

    for period in periods:
        start = period["start"]
        end = resolve_end_date(period["end"], current_date)

        resolved_periods.append({"start": start, "end": end})

    resolved_periods.sort(key=lambda period: period["start"])

    merged = []

    for period in resolved_periods:
        if not merged:
            merged.append(period)
            continue

        last_period = merged[-1]

        if month_index(period["start"]) <= month_index(last_period["end"]) + 1:
            if period["end"] > last_period["end"]:
                last_period["end"] = period["end"]

        else:
            merged.append(period)

    return merged


def calculate_total_experience_months(periods, current_date=None):
    """
    Calculates unique months of professional experience.
    """

    if not periods:
        return 0

    if current_date is None:
        current_date = date.today()

    merged_periods = merge_experience_periods(periods, current_date)

    total_months = 0

    for period in merged_periods:
        start_index = month_index(period["start"])
        end_index = month_index(period["end"])

        total_months += end_index - start_index + 1

    return total_months


def calculate_total_experience_years(periods, current_date=None):
    """
    Calculates unique professional experience in years.
    """

    months = calculate_total_experience_months(periods, current_date)

    return round(months / 12, 2)
