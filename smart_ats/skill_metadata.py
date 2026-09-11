SKILL_DISPLAY_NAMES = {
    "python": "Python",
    "java": "Java",
    "javascript": "JavaScript",
    "typescript": "TypeScript",
    "c++": "C++",
    "c#": "C#",
    "sql": "SQL",
    "mysql": "MySQL",
    "postgresql": "PostgreSQL",
    "mongodb": "MongoDB",
    "redis": "Redis",
    "aws": "AWS",
    "azure": "Azure",
    "docker": "Docker",
    "kubernetes": "Kubernetes",
    "git": "Git",
    "github": "GitHub",
    "linux": "Linux",
    "react": "React",
    "angular": "Angular",
    "vue": "Vue",
    "spring boot": "Spring Boot",
    "django": "Django",
    "flask": "Flask",
    "fastapi": "FastAPI",
    "machine learning": "Machine Learning",
    "artificial intelligence": "Artificial Intelligence",
    "pytorch": "PyTorch",
    "tensorflow": "TensorFlow",
    "ci/cd": "CI/CD",
}

def get_skill_display_name(skill):
    """
    Returns the user-facing display name for a canonical skill.
    """

    return SKILL_DISPLAY_NAMES.get(
        skill,
        skill
    )