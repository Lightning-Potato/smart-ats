import streamlit as st

from smart_ats.skill_metadata import get_skill_display_name


def display_skill_evidence(skill_detail):
    """
    Displays source-based evidence for a matched skill.
    """

    skill_name = get_skill_display_name(
        skill_detail["skill"]
    )

    sources = skill_detail["sources"]

    st.markdown(f"**✓ {skill_name}**")

    if "skills" in sources:
        st.caption("✓ Declared in Skills section")

    if "experience" in sources:
        st.caption("✓ Demonstrated in Experience section")

    if "projects" in sources:
        st.caption("✓ Demonstrated in Projects section")

    if not sources:
        st.caption(
            "○ Skill detected, but no recognized evidence "
            "source was identified"
        )


def display_analysis_dashboard(
    analysis,
    skill_analysis,
    experience_analysis,
    overall_ats_score
):
    """
    Displays the structured ATS analysis in the Streamlit interface.
    """

    st.header("ATS Analysis")

    if overall_ats_score is None:
        st.metric(
            label="Overall ATS Score",
            value="N/A"
        )
    else:
        st.metric(
            label="Overall ATS Score",
            value=f"{overall_ats_score}%"
        )

    st.caption(
        "Overall score is calculated from deterministic "
        "skill and experience matching."
    )

    # -------------------------
    # Match Scores
    # -------------------------

    skill_score = skill_analysis["skill_match_score"]
    experience_score = experience_analysis[
        "experience_match_score"
    ]

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Skill Match Score",
            value=f"{skill_score}%"
        )

    with col2:
        if experience_score is None:
            st.metric(
                label="Experience Match Score",
                value="N/A"
            )
        else:
            st.metric(
                label="Experience Match Score",
                value=f"{experience_score}%"
            )

    st.progress(skill_score / 100)

    # -------------------------
    # Skills Analysis
    # -------------------------

    st.subheader("Skills Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Matched Skills")

        matched_details = skill_analysis[
            "matched_skill_details"
        ]

        if not matched_details:
            st.write("No matched skills detected.")
        else:
            for skill_detail in matched_details:
                display_skill_evidence(skill_detail)

    with col2:
        st.markdown("#### Missing Skills")

        missing_skills = skill_analysis[
            "missing_skills"
        ]

        if not missing_skills:
            st.write("No missing required skills detected.")
        else:
            for skill in missing_skills:
                display_name = get_skill_display_name(skill)
                st.write(f"✗ {display_name}")

    # -------------------------
    # Experience Analysis
    # -------------------------

    st.subheader("Experience Analysis")

    required_years = experience_analysis["required_years"]
    candidate_years = experience_analysis["candidate_years"]

    col1, col2 = st.columns(2)

    with col1:
        if required_years is None:
            st.metric(
                label="Required Experience",
                value="Not specified"
            )
        else:
            st.metric(
                label="Required Experience",
                value=f"{required_years} years"
            )

    with col2:
        st.metric(
            label="Detected Experience",
            value=f"{candidate_years} years"
        )

    if required_years is not None:
        experience_gap = max(
            required_years - candidate_years,
            0
        )

        if experience_gap == 0:
            st.success(
                "The detected experience meets or exceeds "
                "the stated requirement."
            )
        else:
            st.warning(
                f"Experience gap: "
                f"{round(experience_gap, 2)} years"
            )

    # -------------------------
    # AI Insights
    # -------------------------

    st.divider()
    st.header("AI Insights")

    st.subheader("Summary")
    st.write(analysis["summary"])

    st.subheader("Strengths")

    for strength in analysis["strengths"]:
        st.write(f"• {strength}")

    st.subheader("Gaps")

    for gap in analysis["gaps"]:
        st.write(f"• {gap}")

    st.subheader("Recommendations")

    for index, recommendation in enumerate(
        analysis["recommendations"],
        start=1
    ):
        st.write(f"{index}. {recommendation}")