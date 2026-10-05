import streamlit as st
from PyPDF2 import PdfReader

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

# =========================
# DESIGN
# =========================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #f5f7ff, #eef2ff, #faf5ff);
}

.block-container {
    max-width: 1150px;
    padding-top: 35px;
    padding-bottom: 50px;
}

/* HERO */

.hero {
    background: linear-gradient(135deg, #4f46e5, #7c3aed, #9333ea);
    padding: 45px;
    border-radius: 28px;
    color: white;
    box-shadow: 0 15px 40px rgba(79,70,229,0.25);
    margin-bottom: 35px;
}

.hero-badge {
    display: inline-block;
    background: rgba(255,255,255,0.18);
    padding: 7px 14px;
    border-radius: 30px;
    font-size: 13px;
    margin-bottom: 15px;
}

.hero h1 {
    font-size: 46px;
    margin: 0;
    font-weight: 800;
}

.hero p {
    font-size: 18px;
    opacity: 0.9;
}

/* CARDS */

.card {
    background: white;
    padding: 25px;
    border-radius: 22px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 8px 25px rgba(30,41,59,0.07);
    margin-bottom: 20px;
}

.card-title {
    font-size: 21px;
    font-weight: 750;
    color: #172554;
}

.card-subtitle {
    color: #64748b;
    font-size: 14px;
    margin-top: 5px;
    margin-bottom: 15px;
}

/* UPLOAD */

[data-testid="stFileUploader"] {
    background: #f8faff;
    border: 2px dashed #c7d2fe;
    border-radius: 18px;
    padding: 10px;
}

/* BUTTON */

.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 16px;
    border: none;
    background: linear-gradient(90deg, #4f46e5, #7c3aed);
    color: white;
    font-size: 17px;
    font-weight: 700;
    box-shadow: 0 8px 20px rgba(79,70,229,0.25);
}

.stButton > button:hover {
    transform: translateY(-2px);
}

/* RESULTS */

.result-heading {
    text-align: center;
    margin: 40px 0 25px;
}

.result-heading h2 {
    color: #172554;
    font-size: 30px;
}

.result-heading p {
    color: #64748b;
}

/* SCORE */

.score-card {
    background: white;
    border-radius: 24px;
    padding: 30px;
    text-align: center;
    border: 1px solid #e5e7eb;
    box-shadow: 0 8px 25px rgba(30,41,59,0.07);
    margin-bottom: 25px;
}

.score-number {
    font-size: 55px;
    font-weight: 800;
    color: #4f46e5;
}

.score-label {
    color: #64748b;
}

/* SKILLS */

.skill-card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #e5e7eb;
    min-height: 150px;
    box-shadow: 0 7px 20px rgba(30,41,59,0.06);
}

.skill-title {
    font-size: 19px;
    font-weight: 750;
    margin-bottom: 14px;
    color: #172554;
}

.skill {
    display: inline-block;
    padding: 7px 13px;
    margin: 4px;
    border-radius: 30px;
    background: #eef2ff;
    color: #4338ca;
    font-size: 13px;
    font-weight: 650;
}

.missing-skill {
    display: inline-block;
    padding: 7px 13px;
    margin: 4px;
    border-radius: 30px;
    background: #fff1f2;
    color: #be123c;
    font-size: 13px;
    font-weight: 650;
}

/* RECOMMENDATION */

.recommendation {
    background: linear-gradient(135deg, #eef2ff, #faf5ff);
    border: 1px solid #ddd6fe;
    padding: 25px;
    border-radius: 20px;
    margin-top: 25px;
}

.recommendation h3 {
    color: #4338ca;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 13px;
    margin-top: 45px;
}

</style>
""", unsafe_allow_html=True)


# =========================
# HERO
# =========================

st.markdown("""
<div class="hero">
    <div class="hero-badge">✨ AI-Powered Career Tool</div>
    <h1>🤖 AI Resume Analyzer</h1>
    <p>
        Analyze your resume, compare your skills with a job description,
        and discover how well you match the role.
    </p>
</div>
""", unsafe_allow_html=True)


# =========================
# INPUTS
# =========================

col1, col2 = st.columns(2, gap="large")


with col1:

    st.markdown("""
    <div class="card">
        <div class="card-title">📄 Upload Your Resume</div>
        <div class="card-subtitle">
            Upload your latest resume in PDF format.
        </div>
    </div>
    """, unsafe_allow_html=True)

    resume = st.file_uploader(
        "Choose your resume",
        type=["pdf"],
        label_visibility="collapsed"
    )


with col2:

    st.markdown("""
    <div class="card">
        <div class="card-title">💼 Job Description</div>
        <div class="card-subtitle">
            Paste the job description you want to apply for.
        </div>
    </div>
    """, unsafe_allow_html=True)

    job_description = st.text_area(
        "Job Description",
        height=180,
        placeholder="Paste the job description here...",
        label_visibility="collapsed"
    )


# =========================
# BUTTON
# =========================

st.markdown("<br>", unsafe_allow_html=True)

analyze = st.button("🚀  Analyze My Resume")


# =========================
# ANALYSIS
# =========================

if analyze:

    if resume is None:

        st.warning("📄 Please upload your resume first.")

    elif not job_description.strip():

        st.warning("💼 Please enter the job description.")

    else:

        # PDF TEXT

        reader = PdfReader(resume)

        resume_text = ""

        for page in reader.pages:

            text = page.extract_text()

            if text:
                resume_text += text


        # SKILLS

        skills = [
            "python",
            "java",
            "sql",
            "html",
            "css",
            "javascript",
            "mysql",
            "git",
            "github",
            "php",
            "c",
            "c++",
            "machine learning",
            "pandas",
            "excel",
            "power bi",
            "data analysis"
        ]

        resume_lower = resume_text.lower()
        job_lower = job_description.lower()

        resume_skills = []
        job_skills = []

        for skill in skills:

            if skill in resume_lower:
                resume_skills.append(skill)

            if skill in job_lower:
                job_skills.append(skill)


        matched_skills = []

        for skill in job_skills:

            if skill in resume_skills:
                matched_skills.append(skill)


        missing_skills = []

        for skill in job_skills:

            if skill not in resume_skills:
                missing_skills.append(skill)


        # MATCH %

        if len(job_skills) > 0:

            match_percentage = (
                len(matched_skills) /
                len(job_skills)
            ) * 100

        else:

            match_percentage = 0

# =========================
        # RESUME STRENGTH
        # =========================

        resume_strength = 0

        if len(resume_text) > 300:
            resume_strength += 25

        if len(resume_skills) >= 3:
            resume_strength += 25

        if any(word in resume_lower for word in ["project", "projects"]):
            resume_strength += 20

        if any(word in resume_lower for word in ["education", "degree", "b.sc", "mca"]):
            resume_strength += 15

        if any(word in resume_lower for word in ["email", "phone", "contact"]):
            resume_strength += 15


        # =========================
        # RESULTS
        # =========================

        st.markdown("""
        <div class="result-heading">
            <h2>📊 Resume Analysis</h2>
            <p>
                Here's how your resume compares with the job requirements.
            </p>
        </div>
        """, unsafe_allow_html=True)


        # SCORE

        st.markdown(f"""
        <div class="score-card">
            <div class="score-number">
                {match_percentage:.0f}%
            </div>
            <div class="score-label">
                Overall Resume Match
            </div>
        </div>
        """, unsafe_allow_html=True)
# =========================
        # RESUME STRENGTH
        # =========================

        st.markdown(f"""
        <div class="score-card">
            <div class="score-number">
                {resume_strength}%
            </div>
            <div class="score-label">
                Resume Strength
            </div>
        </div>
        """, unsafe_allow_html=True)



        # SKILLS

        col1, col2 = st.columns(2, gap="large")


        with col1:

            st.markdown("""
            <div class="skill-card">
                <div class="skill-title">
                    ✅ Matched Skills
                </div>
            """, unsafe_allow_html=True)

            if matched_skills:

                for skill in matched_skills:

                    st.markdown(
                        f'<span class="skill">{skill.title()}</span>',
                        unsafe_allow_html=True
                    )

            else:

                st.write("No matching skills found.")

            st.markdown("</div>", unsafe_allow_html=True)


        with col2:

            st.markdown("""
            <div class="skill-card">
                <div class="skill-title">
                    ⚠️ Skills to Improve
                </div>
            """, unsafe_allow_html=True)

            if missing_skills:

                for skill in missing_skills:

                    st.markdown(
                        f'<span class="missing-skill">{skill.title()}</span>',
                        unsafe_allow_html=True
                    )

            else:

                st.write("🎉 No missing skills detected!")

            st.markdown("</div>", unsafe_allow_html=True)


        # =========================
        # RECOMMENDATION
        # =========================

        suggestions = []

        if missing_skills:
            for skill in missing_skills:
                suggestions.append(
                    f"Consider learning or improving {skill.title()}."
                )

        if "python" in missing_skills:
            suggestions.append(
                "Practice Python basics, functions, loops and problem-solving."
            )

        if "java" in missing_skills:
            suggestions.append(
                "Learn Java fundamentals and object-oriented programming."
            )

        if "sql" in missing_skills:
            suggestions.append(
                "Practice SQL queries, joins and database concepts."
            )

        if "git" in missing_skills or "github" in missing_skills:
            suggestions.append(
                "Learn basic Git and GitHub commands and practice uploading projects."
            )

        if "html" in missing_skills or "css" in missing_skills:
            suggestions.append(
                "Improve your HTML and CSS fundamentals by creating small web pages."
            )

        if match_percentage >= 80:

            recommendation = """
            🎉 <b>Excellent match!</b><br><br>
            Your resume matches most of the important skills
            mentioned in this job description.
            """

        elif match_percentage >= 50:

            recommendation = """
            👍 <b>Good starting point!</b><br><br>
            Your resume has several matching skills.
            Consider improving the missing skills below.
            """

        else:

            recommendation = """
            💡 <b>There is room for improvement.</b><br><br>
            Consider learning the missing skills and tailoring
            your resume to this job description.
            """

        st.markdown(f"""
        <div class="recommendation">
            <h3>💡 AI Recommendation</h3>
            <p>{recommendation}</p>
        </div>
        """, unsafe_allow_html=True)


        # =========================
        # PERSONALIZED SUGGESTIONS
        # =========================

        if suggestions:

            st.markdown("""
            <div class="recommendation">
                <h3>🎯 Personalized Improvement Suggestions</h3>
            """, unsafe_allow_html=True)

            for suggestion in suggestions:
                st.markdown(f"• {suggestion}")

            st.markdown("</div>", unsafe_allow_html=True)

        else:

            st.success(
                "🎉 Great! No major skill improvements are suggested."
            )


        st.markdown(f"""
        <div class="recommendation">
            <h3>💡 AI Recommendation</h3>
            <p>{recommendation}</p>
        </div>
        """, unsafe_allow_html=True)


        # =========================
        # RESUME TEXT
        # =========================

        st.markdown("<br>", unsafe_allow_html=True)

        with st.expander("📄 View Extracted Resume Text"):

            st.text_area(
                "Extracted Content",
                resume_text,
                height=300
            )


# =========================
# FOOTER
# =========================

st.markdown("""
<div class="footer">
    Built with Python • Streamlit • AI Resume Analysis
</div>
""", unsafe_allow_html=True)
