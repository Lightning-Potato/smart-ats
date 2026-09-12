import re


def extract_required_years(job_description):
    """
    Extracts the minimum explicitly stated years of experience
    from a job description.

    Returns:
        int | None: Required years of experience, or None if no
        explicit requirement is found.
    """

    patterns = [
        r"(\d+)\+?\s+years?\s+of\s+experience",
        r"at\s+least\s+(\d+)\s+years?",
        r"minimum\s+(?:of\s+)?(\d+)\s+years?",
    ]

    for pattern in patterns:
        match = re.search(pattern, job_description, re.IGNORECASE)

        if match:
            return int(match.group(1))

    return None
