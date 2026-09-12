import re

from smart_ats.matching_engine import normalize_skill
from smart_ats.skill_aliases import SKILL_ALIASES
from smart_ats.skill_vocabulary import SKILL_VOCABULARY


def extract_skills(text):
    """
    Extracts known technical skills from raw text.

    Returns:
        list: Skills detected in the text.
    """

    extractable_skills = SKILL_VOCABULARY | set(SKILL_ALIASES.keys())

    detected_skills = []

    for skill in extractable_skills:
        pattern = rf"(?<!\w){re.escape(skill)}(?!\w)"

        if re.search(pattern, text, re.IGNORECASE):
            normalized_skill = normalize_skill(skill)

            if normalized_skill not in detected_skills:
                detected_skills.append(normalized_skill)

    return detected_skills
