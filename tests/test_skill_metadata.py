from smart_ats.skill_metadata import get_skill_display_name


def test_get_skill_display_name():
    assert get_skill_display_name("python") == "Python"
    assert get_skill_display_name("aws") == "AWS"
    assert get_skill_display_name("postgresql") == "PostgreSQL"
    assert get_skill_display_name("javascript") == "JavaScript"


def test_get_unknown_skill_display_name():
    assert get_skill_display_name("unknown skill") == "unknown skill"
