import streamlit as st

from smart_ats.skill_metadata import get_skill_display_name


def display_analysis_dashboard(
    analysis,
    skill_analysis
):
    """
    Displays the structured ATS analysis in the Streamlit interface.
    """

    st.header("ATS Analysis")

    ai_score = analysis["overall_score"]
    skill_score = skill_analysis["skill_match_score"]

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Skill Match Score",
            value=f"{skill_score}%"
        )

    with col2:
        st.metric(
            label="AI Compatibility Assessment",
            value=f"{ai_score}%"
        )

    st.progress(skill_score / 100)

    st.subheader("Summary")
    st.write(analysis["summary"])

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