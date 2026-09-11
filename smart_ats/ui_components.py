import streamlit as st

from smart_ats.skill_metadata import get_skill_display_name


def display_analysis_dashboard(
    analysis,
    skill_analysis,
    experience_analysis
):
    """
    Displays the structured ATS analysis in the Streamlit interface.
    """

    st.header("ATS Analysis")

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

        for skill in skill_analysis["matched_skills"]:
            display_name = get_skill_display_name(skill)
            st.write(f"✓ {display_name}")

    with col2:
        st.markdown("#### Missing Skills")

        for skill in skill_analysis["missing_skills"]:
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