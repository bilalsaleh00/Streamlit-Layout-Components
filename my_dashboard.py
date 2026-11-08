import streamlit as st

st.set_page_config(
    page_title="Study Progress Dashboard",
    page_icon="📚",
    layout="wide"
)

with st.sidebar:
    st.title("Study Controls")

    subject = st.selectbox(
        "Choose Subject",
        ["Python", "SQL", "FastAPI", "Streamlit"]
    )

    study_hours = st.slider(
        "Study Hours This Week",
        min_value=0,
        max_value=20,
        value=5
    )

    show_details = st.checkbox(
        "Show Detailed View",
        value=True
    )

st.title("📚 Study Progress Dashboard")

st.write(
    f"Current subject: **{subject}**"
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Study Hours",
        f"{study_hours} hrs",
        "+2 hrs"
    )

with col2:
    completed_lessons = study_hours * 2

    st.metric(
        "Lessons Completed",
        completed_lessons,
        "+3"
    )

with col3:
    progress = min(study_hours * 5, 100)

    st.metric(
        "Progress",
        f"{progress}%",
        "+5%"
    )

st.divider()

tab1, tab2 = st.tabs(["Overview", "Details"])

with tab1:
    st.subheader("Weekly Overview")

    st.write(
        f"You studied **{study_hours} hours** this week."
    )

    st.progress(progress / 100)

    if progress >= 75:
        st.success("Excellent progress!")
    elif progress >= 40:
        st.info("Good progress. Keep going!")
    else:
        st.warning("Try to add more study time this week.")

with tab2:
    st.subheader("Study Details")

    if show_details:
        st.write(f"Subject: **{subject}**")
        st.write(f"Study Hours: **{study_hours}**")
        st.write(f"Lessons Completed: **{completed_lessons}**")
        st.write(f"Progress: **{progress}%**")
    else:
        st.info(
            "Enable 'Show Detailed View' in the sidebar."
        )

with st.expander("About This Dashboard"):
    st.write(
        "This dashboard tracks study progress using "
        "sidebar controls, metrics, tabs, and progress indicators."
    )

    st.write(
        "Use the sidebar to change the subject, study hours, "
        "and whether detailed information is shown."
    )