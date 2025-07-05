import streamlit as st
from pathlib import Path
from PIL import Image
import base64

st.set_page_config(page_title="Aun Ali Portfolio", page_icon=":briefcase:", layout="wide")  # switched to 'wide'

# --- Custom CSS for Styling Navbar + Removing Padding ---
st.markdown('''
    <style>
        /* NAVBAR */
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #0d1117;
            z-index: 999;
            display: flex;
            justify-content: center;
            align-items: center;    
            height: 55px;
            border-bottom: 1px solid #30363d;
        }
        .navbar a {
            color: #f0f6fc;
            padding: 14px 20px;
            text-decoration: none;
            font-size: 18px;
            transition: background 0.3s ease-in-out;
        }
        .navbar a:hover {
            background-color: #21262d;
            border-radius: 5px;
        }

        /* Main Content Offset */
        .main-content {
            margin-top: 70px;
        }

        /* Remove built-in Streamlit padding */
        .block-container, .main .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }

        /* Image Style */
        .round-image {
            border-radius: 50%;
            width: 180px;
            height: 180px;
            object-fit: cover;
            border: 4px solid #0d6efd;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        .profile-image {
            border-radius: 50%;
            width: 110%;
            max-width: 450px;
            height: auto;
            aspect-ratio: 1/1;
            object-fit: cover;
            border: 5px solid #0d6efd;
            display: block;
            margin: 10px auto 0 100px;
        }
        @media (max-width: 991px) {
            .profile-image {
                margin-left: 0 !important;
            }
        }
        .center-text {
            text-align: center;
        }
            
        
    </style>

    <div class="navbar">
        <a href="#about">About</a>
        <a href="#education">Education</a>
        <a href="#projects">Projects</a>
        <a href="#contact">Contact</a>
    </div>
''', unsafe_allow_html=True)

# --- MAIN CONTENT WRAPPER ---
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# === ABOUT SECTION ===
st.markdown('<a id="about"></a>', unsafe_allow_html=True)
#st.markdown('<h2 class="center-text">👨‍💻 About Me</h2>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2.5])  # Wider right column

# --- Left: Enlarged Profile Image ---
with col1:
    image_path = Path("aunali.jpg")
    if image_path.exists():
        with open(image_path, "rb") as img_file:
            img_bytes = img_file.read()
            img_base64 = base64.b64encode(img_bytes).decode()
        st.markdown(f'''
            <img src="data:image/jpeg;base64,{img_base64}" 
                 class="profile-image"
                 style="border-radius: 50%; width: 500px; height: 400px; object-fit: cover; 
                        border: 5px solid #0d6efd; display: block; margin: 10px auto; margin-left: 100px;" />
        ''', unsafe_allow_html=True)

        # Add Social Icons Below Image
        st.markdown("""
        <div class="social-icons" style="text-align: center; margin-top: 20px; margin-left: 165px;">
            <a href="https://github.com/aunali6783" target="_blank" style="margin-right: 1px;">
                <img src="https://images.seeklogo.com/logo-png/50/1/github-icon-logo-png_seeklogo-503247.png" width="40"/>
            </a>
            <a href="https://www.linkedin.com/in/raja-aun-ali-khan-ab80b1248/" target="_blank" style="margin-right: 1px;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" width="40"/>
            </a>
            <a href="https://www.instagram.com/aunnn_ali_/" target="_blank" style="margin-right: 1px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="40"/>
            </a>
            <a href="https://www.facebook.com/raja.a.ali.1004" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" width="40"/>
            </a>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.warning("⚠️ Profile picture not found. Make sure 'aunali.jpg' is in the same folder.")


# --- Right: Expanded Intro Text ---
with col2:
    st.markdown("""
        <style>
        .intro-section {
            display: flex;
            flex-direction: column;
           
            max-width: 800px;
            width: 50%;
            margin-left: auto !important;
            margin-right: auto !important;
        }
        .resume-btn {
            margin-top: 5px;
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .stDownloadButton > button {
            display: block;
            margin: 10px auto 0 auto; /* top margin and centered horizontally */
            background: linear-gradient(90deg, #0d6efd, #00c8ff);
            color: #fff;
            font-size: 18px;
            font-weight: 600;
            border: none;
            border-radius: 8px;
            padding: 12px 32px;
            box-shadow: 0 2px 8px rgba(13,110,253,0.10);
            transition: background 0.2s, box-shadow 0.2s;
            cursor: pointer;
        }

        }
        .stDownloadButton > button:hover {
            background: linear-gradient(90deg, #00c8ff, #0d6efd);
            box-shadow: 0 4px 16px rgba(13,110,253,0.18);
        }
        </style>
        <div class="intro-section">
            <h2 style='font-size:40px; margin-bottom: 0; margin-left: 0; text-align: center;'>Raja Aun Ali Khan</h2>
            <p style='font-size: 18px; margin-top: 30px; margin-left: 0; margin-right: 0; margin-buttom:0;'>
            🚀 I'm an aspiring AI Developer with a strong interest in Artificial Intelligence and Machine Learning.<br>
            Passionate about building smart systems that solve real-world problems using data and code.<br>
            I'm constantly exploring new tools, algorithms, and deep learning frameworks like PyTorch.<br>
            Eager to grow, collaborate, and contribute to impactful tech solutions that make a difference.<br>
            Currently pursuing my BS in Computer Science from FAST NUCES Lahore (2022–2026). 🌟
            </p>
    """, unsafe_allow_html=True)

    # Add Resume Download Button (centered below paragraph)
    resume_path = Path("AunAli_Resume.pdf")
    if resume_path.exists():
        with open(resume_path, "rb") as f:
            resume_bytes = f.read()
        st.markdown('<div class="resume-btn">', unsafe_allow_html=True)
        st.download_button(
            label="📄 Download Resume",
            data=resume_bytes,
            file_name="Raja_Aun_Ali_Khan_Resume.pdf",
            mime="application/pdf",
            key="download_resume_btn"
        )
        st.markdown('</div></div>', unsafe_allow_html=True)
    else:
        st.markdown('</div>', unsafe_allow_html=True)
        st.warning("Resume file not found. Please add 'AunAli_Resume.pdf' to the project folder.")






# === ABOUT + SKILLS SECTION ===
# CSS for about-container and skills
st.markdown("""
<style>
    .about-container {
        background-color: #161b22;
        border-radius: 15px;
        padding: 30px;
        margin: 50px 40px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        color: #c9d1d9;
    }
    .about-title {
        font-size: 40px;
        color: #0d6efd;
        font-weight: 700;
        margin-bottom: 20px;
    }
    .about-text {
        font-size: 18px;
        line-height: 1.8;
        margin-bottom: 30px;
        color: #d0d6dc;
    }
    .skill-title {
        font-size: 20px;
        font-weight: 600;
        margin-bottom: 6px;
        color: #f0f6fc;
    }
    .progress-bar {
        background-color: #30363d;
        border-radius: 10px;
        height: 18px;
        margin-bottom: 20px;
        overflow: hidden;
    }
    .progress-fill {
        height: 100%;
        border-radius: 10px;
        background: linear-gradient(90deg, #0d6efd, #00c8ff);
        transition: width 1s ease-in-out;
    }
</style>
""", unsafe_allow_html=True)

# About text (markdown or HTML)
st.markdown("""
<div class="about-container">
    <div class="about-title">   About Me</div>
    <div class="about-text">
        I'm <strong>Aun Ali</strong>, an enthusiastic and ambitious AI developer from Pakistan 🇵🇰. <br>
        My core passion lies at the intersection of <strong>Artificial Intelligence</strong> and <strong>Web Development</strong>, where I love building things that can think, predict, and adapt.<br><br>
        Currently pursuing a BS in Computer Science at FAST NUCES Lahore (2022–2026), I’m constantly upgrading my toolkit — from neural networks in <strong>PyTorch</strong> to stunning UIs in <strong>React</strong>. I'm self-driven, quick to learn, and always up for a challenge.<br><br>
        When I'm not coding, you’ll find me reading about emerging tech, experimenting with new frameworks, or designing a full-stack system just for fun. My goal? Build impactful solutions, join communities that innovate, and contribute to real-world AI transformation.
    </div>
</div>
""", unsafe_allow_html=True)

# Skills section as HTML (for proper rendering)
skills_html = """
<style>
    .about-container {
        background-color: #161b22;
        border-radius: 15px;
        padding: 30px;
        margin: 50px 40px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        color: #c9d1d9;
    }
    .about-title {
        font-size: 40px;
        color: #0d6efd;
        font-weight: 700;
        margin-bottom: 20px;
    }
    .skill-title {
        font-size: 22px;
        font-weight: 600;
        margin-bottom: 6px;
        color: #f0f6fc;
        display: flex;
        align-items: center;
        gap: 10px;
        justify-content: center;
    }
    .badge {
        display: inline-block;
        background: linear-gradient(90deg, #0d6efd, #00c8ff);
        color: #fff;
        font-size: 13px;
        font-weight: 600;
        border-radius: 8px;
        padding: 2px 10px;
        margin-left: 10px;
        margin-right: 5px;
        vertical-align: middle;
        box-shadow: 0 2px 6px rgba(13,110,253,0.12);
        letter-spacing: 0.5px;
        transition: background 0.3s;
    }
    .badge-learning {
        background: linear-gradient(90deg, #ff9800, #ffc107);
        color: #222;
    }
    .badge-collab {
        background: linear-gradient(90deg, #00c8ff, #0d6efd);
        color: #fff;
    }
    .product-badge {
        display: inline-block;
        vertical-align: middle;
        margin-left: 6px;
        margin-right: 2px;
        height: 22px;
        width: 22px;
        border-radius: 4px;
        background: #fff;
        box-shadow: 0 1px 4px rgba(0,0,0,0.08);
        object-fit: contain;
    }
    .progress-bar {
        background-color: #30363d;
        border-radius: 12px;
        height: 32px;
        width: 100%;
        max-width: 500px;
        margin: 0 auto 28px auto;
        overflow: hidden;
        transition: box-shadow 0.3s;
        display: flex;
        align-items: center;
    }
    .progress-bar:hover {
        box-shadow: 0 0 0 3px #0d6efd44;
    }
    .progress-fill {
        height: 100%;
        border-radius: 12px;
        background: linear-gradient(90deg, #0d6efd, #00c8ff);
        transition: width 1.2s cubic-bezier(.4,2,.6,1), background 0.3s;
    }
    .progress-bar:hover .progress-fill {
        background: linear-gradient(90deg, #ff9800, #0d6efd);
        animation: fillPulse 1.2s;
    }
    @keyframes fillPulse {
        0% { filter: brightness(1); }
        50% { filter: brightness(1.3); }
        100% { filter: brightness(1); }
    }
</style>
<div class="about-container">
    <div class="about-title">📈 My Skills</div>
    <div>
        <div class="skill-title">Web Development (Frontend)
            <img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg' class='product-badge' title='React'/>
            <span class="badge badge-collab">Open to Collaborate</span>
        </div>
        <div class="progress-bar"><div class="progress-fill" style="width: 70%;"></div></div>

        <div class="skill-title">PyTorch / Deep Learning
            <img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytorch/pytorch-original.svg' class='product-badge' title='PyTorch'/>
            <span class="badge badge-learning">Currently Learning</span>
        </div>
        <div class="progress-bar"><div class="progress-fill" style="width: 50%;"></div></div>

        <div class="skill-title">C++ Programming
            <img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg' class='product-badge' title='C++'/>
        </div>
        <div class="progress-bar"><div class="progress-fill" style="width: 80%;"></div></div>

        <div class="skill-title">Data Analysis (Pandas / NumPy)
            <img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg' class='product-badge' title='Python'/>
        </div>
        <div class="progress-bar"><div class="progress-fill" style="width: 65%;"></div></div>

        <div class="skill-title">Machine Learning (Scikit-learn)
            <img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg' class='product-badge' title='Python'/>
            <span class="badge badge-learning">Currently Learning</span>
        </div>
        <div class="progress-bar"><div class="progress-fill" style="width: 60%;"></div></div>

        <div class="skill-title">Git & GitHub
            <img src='https://images.seeklogo.com/logo-png/50/1/github-icon-logo-png_seeklogo-503247.png' class='product-badge' title='GitHub'/>
        </div>
        <div class="progress-bar"><div class="progress-fill" style="width: 75%;"></div></div>
    </div>
</div>
"""
import streamlit.components.v1 as components
components.html(skills_html, height=600)

# === EDUCATION SECTION ===
st.markdown("""
<style>
.education-container {
    background: #161b22;
    border-radius: 15px;
    padding: 32px 32px 18px 32px;
    margin: 40px 0 32px 0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.18);
    color: #c9d1d9;
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
}
.edu-title {
    font-size: 28px;
    font-weight: 700;
    color: #0d6efd;
    margin-bottom: 18px;
    text-align: left;
    letter-spacing: 0.5px;
}
.edu-entry {
    background: #21262d;
    border-radius: 10px;
    padding: 18px 22px 12px 22px;
    margin-bottom: 18px;
    box-shadow: 0 2px 8px rgba(13,110,253,0.07);
    transition: box-shadow 0.2s;
}
.edu-entry:hover {
    box-shadow: 0 4px 16px rgba(13,110,253,0.13);
}
.edu-entry h4 {
    margin: 0 0 6px 0;
    font-size: 20px;
    color: #f0f6fc;
    font-weight: 600;
}
.edu-entry p {
    margin: 0 0 4px 0;
    font-size: 15px;
    color: #d0d6dc;
    line-height: 1.6;
}
@media (max-width: 767px) {
    .education-container {
        padding: 16px 4px 10px 4px;
        max-width: 100%;
    }
    .edu-title {
        font-size: 22px;
        text-align: center;
    }
    .edu-entry {
        padding: 12px 8px 8px 8px;
    }
    .edu-entry h4 {
        font-size: 17px;
    }
    .edu-entry p {
        font-size: 13px;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="education-container">\
        <div class="edu-title">Education Background</div>\
        <div class="edu-entry">\
            <h4>The Trust School, Lahore</h4>\
            <p>Matric in Science Group | Marks: 1055/1100 | Grade: A+ | 2018–2020</p>\
        </div>\
        <div class="edu-entry">\
            <h4>Government College University (GCU), Lahore</h4>\
            <p>Intermediate in Pre-Engineering | Marks: 1027/1100 | Grade: A+ | 2020–2022</p>\
        </div>\
        <div class="edu-entry">\
            <h4>FAST NUCES, Lahore</h4>\
            <p>B.S. in Computer Science | Junior | 6th semester | June 2022 – Ongoing</p>\
            <p><strong>Relevant Coursework:</strong> Data Structures and Algorithms, Database Systems, Programming Fundamentals, Operating Systems, Object Oriented Programming, Communication and Presentation Skills, Computer Organization and Assembly Language (COAL), Software Design and Analysis, Design and Analysis of Algorithms (DSA), Entrepreneurship.</p>\
        </div>\
    </div>',
    unsafe_allow_html=True
)


# === PROJECTS SECTION ===
st.markdown("""
<style>
.projects-container {
    background: #161b22;
    border-radius: 15px;
    padding: 32px 32px 18px 32px;
    margin: 40px 0 32px 0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.18);
    color: #c9d1d9;
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
}
.projects-title {
    font-size: 28px;
    font-weight: 700;
    color: #0d6efd;
    margin-bottom: 18px;
    text-align: left;
    letter-spacing: 0.5px;
}
.project-card {
    background: #21262d;
    border-radius: 10px;
    padding: 18px 22px 12px 22px;
    margin-bottom: 18px;
    box-shadow: 0 2px 8px rgba(13,110,253,0.07);
    display: flex;
    align-items: flex-start;
    gap: 18px;
    transition: box-shadow 0.2s;
}
.project-card:hover {
    box-shadow: 0 4px 16px rgba(13,110,253,0.13);
}
.project-icon {
    font-size: 32px;
    margin-top: 2px;
    color: #0d6efd;
    min-width: 36px;
}
.project-info {
    flex: 1;
}
.project-title {
    font-size: 18px;
    font-weight: 600;
    color: #f0f6fc;
    margin-bottom: 4px;
}
.project-desc {
    font-size: 15px;
    color: #d0d6dc;
    margin: 0;
}
@media (max-width: 767px) {
    .projects-container {
        padding: 16px 4px 10px 4px;
        max-width: 100%;
    }
    .projects-title {
        font-size: 22px;
        text-align: center;
    }
    .project-card {
        padding: 12px 8px 8px 8px;
        gap: 10px;
    }
    .project-icon {
        font-size: 26px;
        min-width: 28px;
    }
    .project-title {
        font-size: 15px;
    }
    .project-desc {
        font-size: 13px;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="projects-container">
    <div class="projects-title">Projects</div>
    <div class="project-card">
        <div class="project-icon">⚙️</div>
        <div class="project-info">
            <div class="project-title">Management System using OOP Concepts</div>
            <div class="project-desc">A desktop application demonstrating core Object-Oriented Programming principles for efficient management tasks.</div>
        </div>
    </div>
    <div class="project-card">
        <div class="project-icon">🎮</div>
        <div class="project-info">
            <div class="project-title">Snake Game using Assembly Language</div>
            <div class="project-desc">A classic Snake game built from scratch in Assembly, showcasing low-level programming and graphics handling.</div>
        </div>
    </div>
    <div class="project-card">
        <div class="project-icon">🗳️</div>
        <div class="project-info">
            <div class="project-title">Online Voting System using Concepts of SDA</div>
            <div class="project-desc">A secure online voting platform leveraging data structures and algorithms for real-time, reliable elections.</div>
        </div>
    </div>
    <div class="project-card">
        <div class="project-icon">🗄️</div>
        <div class="project-info">
            <div class="project-title">Election Management System with Database</div>
            <div class="project-desc">A full-featured system for managing elections, candidates, and results, backed by a robust database.</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# === CONTACT SECTION ===
st.markdown('<a id="contact"></a>', unsafe_allow_html=True)
st.markdown("""
<style>
.contact-container {
    background: #161b22;
    border-radius: 15px;
    padding: 32px 32px 18px 32px;
    margin: 40px 0 32px 0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.18);
    color: #c9d1d9;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}
.contact-title {
    font-size: 28px;
    font-weight: 700;
    color: #0d6efd;
    margin-bottom: 18px;
    text-align: left;
    letter-spacing: 0.5px;
}
.contact-method {
    display: flex;
    align-items: center;
    gap: 16px;
    background: #21262d;
    border-radius: 10px;
    padding: 14px 20px;
    margin-bottom: 14px;
    box-shadow: 0 2px 8px rgba(13,110,253,0.07);
    transition: box-shadow 0.2s;
}
.contact-method:hover {
    box-shadow: 0 4px 16px rgba(13,110,253,0.13);
}
.contact-icon-img {
    width: 28px;
    height: 28px;
    display: block;
    border-radius: 6px;
    background: #fff;
    box-shadow: 0 1px 4px rgba(13,110,253,0.10);
}
.contact-link {
    color: #58a6ff;
    font-size: 16px;
    font-weight: 500;
    text-decoration: none;
    transition: color 0.2s;
    word-break: break-all;
}
.contact-link:hover {
    color: #1f6feb;
    text-decoration: underline;
}
.contact-phone {
    color: #d0d6dc;
    font-size: 16px;
    font-weight: 500;
    word-break: break-all;
}
@media (max-width: 767px) {
    .contact-container {
        padding: 16px 4px 10px 4px;
        max-width: 100%;
    }
    .contact-title {
        font-size: 22px;
        text-align: center;
    }
    .contact-method {
        padding: 10px 8px;
        gap: 10px;
    }
    .contact-icon-img {
        width: 22px;
        height: 22px;
    }
    .contact-link, .contact-phone {
        font-size: 14px;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="contact-container">
    <div class="contact-title">Contact</div>
    <div class="contact-method">
        <img class="contact-icon-img" src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" alt="Gmail" />
        <a class="contact-link" href="https://mail.google.com/mail/?view=cm&fs=1&to=rajaaunalikhan@gmail.com" target="_blank">rajaaunalikhan@gmail.com</a>
    </div>
    <div class="contact-method">
        <img class="contact-icon-img" src="https://images.seeklogo.com/logo-png/50/1/github-icon-logo-png_seeklogo-503247.png" alt="GitHub" />
        <a class="contact-link" href="https://github.com/aunali6783" target="_blank">@aunali6783</a>
    </div>
    <div class="contact-method">
        <img class="contact-icon-img" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" alt="LinkedIn" />
        <a class="contact-link" href="https://www.linkedin.com/in/raja-aun-ali-khan-ab80b1248/" target="_blank">LinkedIn: Raja Aun Ali Khan</a>
    </div>
    <div class="contact-method">
        <img class="contact-icon-img" src="https://cdn-icons-png.flaticon.com/512/597/597177.png" alt="Phone" />
        <span class="contact-phone">03209486621</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- END MAIN CONTENT ---
st.markdown('</div>', unsafe_allow_html=True)