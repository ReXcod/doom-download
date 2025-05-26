import streamlit as st

# Page setup
st.set_page_config(page_title="Download DOOM", page_icon="💾", layout="centered")

# App UI
st.markdown("""
    <div style="background-color:#fff;padding:2rem;border-radius:1rem;text-align:center;box-shadow:0 0 10px rgba(0,0,0,0.1)">
        <h2>🎮 Download DOOM Installer</h2>
        <p>Get your copy of the installer below.</p>
        <a href="https://vitedu-my.sharepoint.com/:u:/g/personal/rohan_sonwane24_vit_edu/EU4gmtz8hKtIs1DsPRiZrjMBztfgBKhFCfh1tH8AHiWHPQ?e=MJniNh" target="_blank">
            <button style="padding:10px 20px;font-size:16px;border:none;background-color:#4CAF50;color:white;border-radius:8px;cursor:pointer;">
                ⬇️ Download DOOM.exe
            </button>
        </a>
    </div>
""", unsafe_allow_html=True)
