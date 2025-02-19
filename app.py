

import streamlit as st
import random
import pandas as pd
from datetime import datetime

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
        padding: 20px;
        border-radius: 10px;
    }
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #ffffff, #f0f0f0);
        padding: 20px;
        border-radius: 10px;
    }
    h1, h2, h3 {
        color: #2c3e50;
        font-family: 'Arial', sans-serif;
    }
    .stButton button {
        background: linear-gradient(135deg, #6a11cb, #2575fc);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #2575fc, #6a11cb);
    }
    .stProgress > div > div > div {
        background: linear-gradient(135deg, #6a11cb, #2575fc);
    }
    .stMarkdown {
        font-size: 16px;
        color: #2c3e50;
    }
    .card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .profile-card {
        background: linear-gradient(135deg, #6a11cb, #2575fc);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    .badge-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .badge {
        display: inline-block;
        background: #6a11cb;
        color: white;
        padding: 5px 10px;
        border-radius: 20px;
        margin: 5px;
        font-size: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Session State for User Data
if "users" not in st.session_state:
    st.session_state.users = {}

# App Logo and Title
col1, col2 = st.columns([1,1])

# Center-Aligned Heading
st.markdown("<h1 style='text-align: center; color: #2c3e50; margin-bottom: 10px;'>🚀 Growth Mindset Challenge</h1>", unsafe_allow_html=True)

# Center-Aligned Subheading
st.markdown("<h2 style='text-align: center; color: #6a11cb;'>Master Programming, Transform Your Future! 💻</h2>", unsafe_allow_html=True)

# Right-Aligned Heading on Next Line
st.markdown("<h3 style='text-align: center; color: #2c3e50;'>💻 Welcome to the Programming Learning Adventure!</h3>", unsafe_allow_html=True)

# Centered Instruction
st.markdown("<p style='text-align: center; font-size: 18px; color: #34495e;'>Enter your coder name in the sidebar to begin your journey!</p>", unsafe_allow_html=True)



# Sidebar - User Profile
st.sidebar.markdown("<h2 style='color: #ffff;'>👤 Your Profile</h2>", unsafe_allow_html=True)
name = st.sidebar.text_input("Enter Coder name")
goal = st.sidebar.text_input("What's your biggest learning goal?")
learning_style = st.sidebar.selectbox(
    "How do you learn best?", ["Visual", "Reading/Writing", "Hands-on", "Listening"]
)
profile_pic = st.sidebar.file_uploader("Upload a profile picture", type=["jpg", "jpeg", "png"])
bio = st.sidebar.text_area("Write a short bio about yourself")
interests = st.sidebar.text_input("What are your interests? (e.g., coding, art, science)")
email = st.sidebar.text_input("Your email (optional)")

# Center & Right-Aligned Headings


if name:
    if name not in st.session_state.users:
        st.session_state.users[name] = {
            "effort": 5,
            "learning": 5,
            "feedback": "",
            "milestones": [],
            "badges": [],
            "mood": "😊",
            "weekly_reflection": "",
            "profile_pic": None,
            "bio": "",
            "interests": "",
            "email": "",
        }

    # Update user profile data
    st.session_state.users[name]["profile_pic"] = profile_pic
    st.session_state.users[name]["bio"] = bio
    st.session_state.users[name]["interests"] = interests
    st.session_state.users[name]["email"] = email
    
    # User Profile Card
    st.markdown("<div class='profile-card'><h2 style='color: white;'>👤 Your Profile</h2>", unsafe_allow_html=True)
    if st.session_state.users[name]["profile_pic"]:
        st.image(st.session_state.users[name]["profile_pic"], width=100)
    st.markdown(f"<h3 style='color: white;'>🌟 Welcome, {name}!</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: white;'>Your Goal: <i>{goal}</i></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: white;'>Learning Style: <i>{learning_style}</i></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: white;'>Bio: <i>{bio}</i></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: white;'>Interests: <i>{interests}</i></p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: white;'>Email: <i>{email}</i></p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)