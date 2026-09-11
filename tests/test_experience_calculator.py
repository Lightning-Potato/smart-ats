from datetime import date

from smart_ats.experience_calculator import (
    calculate_total_experience_months,
    calculate_total_experience_years,
    merge_experience_periods,
)

def test_calculate_single_experience_period():
    periods = [
        {
            "start": date(2022, 1, 1),
            "end": date(2022, 12, 1)
        }
    ]

    assert calculate_total_experience_months(
        periods
    ) == 12

def test_calculate_non_overlapping_periods():
    periods = [
        {
            "start": date(2021, 1, 1),
            "end": date(2021, 12, 1)
        },
        {
            "start": date(2023, 1, 1),
            "end": date(2023, 12, 1)
        }
    ]

    assert calculate_total_experience_months(
        periods
    ) == 24

def test_overlapping_periods_are_not_double_counted():
    periods = [
        {
            "start": date(2022, 1, 1),
            "end": date(2023, 12, 1)
        },
        {
            "start": date(2023, 1, 1),
            "end": date(2024, 12, 1)
        }
    ]

    assert calculate_total_experience_months(
        periods
    ) == 36

def test_continuous_periods_are_merged():
    periods = [
        {
            "start": date(2022, 1, 1),
            "end": date(2022, 12, 1)
        },
        {
            "start": date(2023, 1, 1),
            "end": date(2023, 12, 1)
        }
    ]

    merged = merge_experience_periods(
        periods,
        date(2026, 9, 1)
    )

    assert len(merged) == 1

def test_current_job_uses_supplied_current_date():
    periods = [
        {
            "start": date(2025, 1, 1),
            "end": None
        }
    ]

    months = calculate_total_experience_months(
        periods,
        current_date=date(2025, 12, 1)
    )

    assert months == 12

def test_empty_experience_periods():
    assert calculate_total_experience_months([]) == 0
    assert calculate_total_experience_years([]) == 0.0

def test_calculate_experience_years():
    periods = [
        {
            "start": date(2022, 1, 1),
            "end": date(2023, 6, 1)
        }
    ]

    assert calculate_total_experience_years(
        periods
    ) == 1.5