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
                 style="border-radius: 50%; width: 500px; height: 500px; object-fit: cover; 
                        border: 5px solid #0d6efd; display: block; margin: 10px auto; margin-left: 100px;" />
        ''', unsafe_allow_html=True)

        # Add Social Icons Below Image
        st.markdown("""
        <div style="text-align: center; margin-top: 40px; margin-left: 150px;">
            <a href="https://github.com/aunali6783" target="_blank" style="margin-right: 12px;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="65"/>
            </a>
            <a href="https://linkedin.com/in/aunali6783" target="_blank" style="margin-right: 12px;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" width="65"/>
            </a>
            <a href="https://instagram.com/aunali_6783" target="_blank" style="margin-right: 12px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="65"/>
            </a>
            <a href="https://facebook.com/aunali6783" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" width="65"/>
            </a>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.warning("⚠️ Profile picture not found. Make sure 'aunali.jpg' is in the same folder.")


# --- Right: Expanded Intro Text ---
with col2:
    st.markdown("""
        <h2 style='font-size: 70px; margin-bottom: 0; margin-left: 300px;'>Raja Aun Ali Khan   </h2>
        <p style='font-size: 25px; margin-top: 70px; margin-left: 200px; margin-right: 150px; text-align: center;'>
        🚀 I'm an aspiring AI Developer with a strong interest in Artificial Intelligence and Machine Learning.
Passionate about building smart systems that solve real-world problems using data and code.
I'm constantly exploring new tools, algorithms, and deep learning frameworks like PyTorch.
Eager to grow, collaborate, and contribute to impactful tech solutions that make a difference.
Currently pursuing my BS in Computer Science from FAST NUCES Lahore (2022–2026). 🌟
        </p>
    """, unsafe_allow_html=True)






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
    <div class="about-title">🧠 About Me</div>
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
        width: 1500px;
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
            <img src='https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg' class='product-badge' title='GitHub'/>
        </div>
        <div class="progress-bar"><div class="progress-fill" style="width: 75%;"></div></div>
    </div>
</div>
"""
import streamlit.components.v1 as components
components.html(skills_html, height=600)

# === EDUCATION SECTION ===
st.markdown('<a id="education"></a>', unsafe_allow_html=True)
st.header("🎓 Education")
st.write("""
- **BS Computer Science** — FAST NUCES Lahore (2021–2025)
- Relevant Courses: Machine Learning, Distributed Systems, Deep Learning, Data Structures
""")


# === PROJECTS SECTION ===
st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
st.header("🛠 Projects")
st.markdown("""
- **Face Recognition System** using PyTorch + FaceNet  
- **AI-powered 3D Portfolio** with React, Tailwind, and Three.js  
- **Online Voting System** built using React + Firebase  
""")

# === CONTACT SECTION ===
st.markdown('<a id="contact"></a>', unsafe_allow_html=True)
st.header("📬 Contact")
st.markdown("""
- 📧 Email: [rajaaunalikhan@gmail.com](mailto:rajaaunalikhan@gmail.com)  
- 💼 GitHub: [@aunali6783](https://github.com/aunali6783)  
- 🧠 LinkedIn: [Aun Ali](https://linkedin.com/in/aunali6783)
""")

# --- END MAIN CONTENT ---
st.markdown('</div>', unsafe_allow_html=True)