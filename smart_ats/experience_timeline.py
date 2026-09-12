import re
from datetime import date

MONTHS = {
    "jan": 1,
    "january": 1,
    "feb": 2,
    "february": 2,
    "mar": 3,
    "march": 3,
    "apr": 4,
    "april": 4,
    "may": 5,
    "jun": 6,
    "june": 6,
    "jul": 7,
    "july": 7,
    "aug": 8,
    "august": 8,
    "sep": 9,
    "sept": 9,
    "september": 9,
    "oct": 10,
    "october": 10,
    "nov": 11,
    "november": 11,
    "dec": 12,
    "december": 12,
}


def parse_month_year(month_text, year_text):
    """
    Converts a month name and year into a date object.
    """

    month = MONTHS[month_text.lower()]
    year = int(year_text)

    return date(year, month, 1)


def extract_experience_periods(resume_text):
    """
    Extracts supported employment date ranges from resume text.

    Returns:
        list: Employment periods with start and end dates.
    """

    month_pattern = (
        r"Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|"
        r"Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|"
        r"Aug(?:ust)?|Sep(?:t(?:ember)?)?|"
        r"Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?"
    )

    pattern = rf"""
        ({month_pattern})\s+(\d{{4}})
        \s*[-–]\s*
        (?:
            ({month_pattern})\s+(\d{{4}})
            |
            (Present|Current)
        )
    """

    matches = re.findall(pattern, resume_text, re.IGNORECASE | re.VERBOSE)

    periods = []

    for match in matches:
        start_month = match[0]
        start_year = match[1]
        end_month = match[2]
        end_year = match[3]
        present_marker = match[4]

        start_date = parse_month_year(start_month, start_year)

        if present_marker:
            end_date = None
        else:
            end_date = parse_month_year(end_month, end_year)

        periods.append({"start": start_date, "end": end_date})

    return periods
