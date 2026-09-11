import streamlit as st


def display_analysis_dashboard(analysis):
    """
    Displays the structured ATS analysis in the Streamlit interface.
    """

    st.header("ATS Analysis")

    score = analysis["overall_score"]

    st.metric(
        label="Overall Match Score",
        value=f"{score}%"
    )

    st.progress(score / 100)

    st.subheader("Summary")
    st.write(analysis["summary"])

    st.subheader("Skills Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Matched Skills")

        for skill in analysis["matched_skills"]:
            st.write(f"✓ {skill}")

    with col2:
        st.markdown("#### Missing Skills")

        for skill in analysis["missing_skills"]:
            st.write(f"✗ {skill}")

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