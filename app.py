import streamlit as st
import pandas as pd

st.title("AI-Based Communication & Soft Skill Trainer")
st.write("Welcome! Upload your video to get feedback.")

uploaded_video = st.file_uploader(
    "Upload your communication video",
    type=["mp4", "mov", "avi"]
)

if uploaded_video is not None:
    st.video(uploaded_video)

    st.subheader("Communication Feedback")

    st.metric("Facial Expression Score", "78 / 100")
    st.metric("Tone & Emotion Score", "82 / 100")
    st.metric("Overall Communication Score", "80 / 100")

    st.write("✅ Good eye contact")
    st.write("⚠️ Improve voice clarity")

    # ---- CSV REPORT PART (IMPORTANT) ----
    report_data = {
        "Facial Score": [78],
        "Tone Score": [82],
        "Overall Score": [80]
    }

    df = pd.DataFrame(report_data)

    st.success("Report generated successfully!")

    st.download_button(
        label="Download Feedback Report (CSV)",
        data=df.to_csv(index=False),
        file_name="communication_report.csv",
        mime="text/csv"
    )

