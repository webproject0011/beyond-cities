import streamlit as st
from supabase import create_client
from streamlit_searchbox import st_searchbox

# --- CONFIGURATION ---
URL = "https://jviofuoluvrnpnyhdals.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imp2aW9mdW9sdXZybnBueWhkYWxzIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3NzI3NDkwMywiZXhwIjoyMDkyODUwOTAzfQ.9pPF_oD6fljfQXQSDJbgKs414EYt5lm8aqOxCRW1lUQ"
supabase = create_client(URL, KEY)

# --- PAGE CONFIG ---
st.set_page_config(page_title="Beyond Cities | Urban Intelligence", page_icon="🌃", layout="centered")

# --- CSS (High-End Urban Night Theme) ---
st.markdown("""
    <style>
    /* Premium City Night Background */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.8)), 
                    url('https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?q=80&w=2088&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .header-container { text-align: center; padding: 70px 0 30px 0; }
    
    .main-title {
        color: #ffffff !important;
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 4.5rem !important;
        font-weight: 900;
        letter-spacing: -2px;
        margin-bottom: 0px;
        text-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    .subtitle {
        color: #00d2ff !important;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 5px;
        font-weight: 600;
        opacity: 0.9;
    }

    /* Modern Glassmorphism Container */
    .result-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 45px;
        margin-top: 40px;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.4);
    }

    .village-name {
        color: #ffffff;
        font-size: 2.6rem;
        font-weight: 800;
        margin-bottom: 30px;
        letter-spacing: -1px;
    }

    .data-row {
        display: flex;
        justify-content: space-between;
        padding: 15px 0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }

    .data-label { color: rgba(255, 255, 255, 0.4); font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1.5px; }
    .data-value { color: #00d2ff; font-weight: 600; font-size: 1.15rem; }

    /* Realistic Minimalist Footer */
    .footer {
        position: fixed;
        left: 0; bottom: 0; width: 100%;
        background: rgba(0, 0, 0, 0.9);
        color: rgba(255, 255, 255, 0.5);
        text-align: center;
        padding: 18px 0;
        font-size: 0.75rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        border-top: 1px solid rgba(255, 255, 255, 0.05);
    }
    .footer b { color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
    <div class="header-container">
        <h1 class="main-title">BEYOND CITIES</h1>
        <p class="subtitle">Rural Data Intelligence Engine</p>
    </div>
    """, unsafe_allow_html=True)

# --- INSTANT SEARCH FUNCTION ---
def search_villages(search_term: str):
    if not search_term or len(search_term) < 1:
        return []
    term = search_term.strip().capitalize()
    try:
        res = supabase.table('villages').select('name, sub_districts(name, districts(name, states(name)))').like('name', f'{term}%').limit(10).execute()
        return [(f"📍 {v['name']} ({v['sub_districts']['districts']['name']})", v) for v in res.data]
    except:
        return []

# --- SEARCHBOX ---
selected_village = st_searchbox(
    search_villages,
    placeholder="Search 600,000+ villages instantly...",
    key="city_night_v1"
)

# --- DISPLAY LOGIC ---
if selected_village:
    v = selected_village
    st.markdown(f"""
    <div class="result-card">
        <div class="village-name">{v['name'].upper()}</div>
        <div class="data-row"><span class="data-label">State</span><span class="data-value">{v['sub_districts']['districts']['states']['name']}</span></div>
        <div class="data-row"><span class="data-label">District</span><span class="data-value">{v['sub_districts']['districts']['name']}</span></div>
        <div class="data-row"><span class="data-label">Tehsil</span><span class="data-value">{v['sub_districts']['name']}</span></div>
    </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
    <div class="footer">
        © 2026 Beyond Cities Intelligence | Developed by <b>ABHISHEK DUBEY</b>
    </div>
    """, unsafe_allow_html=True)