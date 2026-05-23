import streamlit as st

# 1. Page Configuration Architecture
st.set_page_config(
    page_title="GlobalInternet.py | Flight Launch Engine",
    page_icon="✈️",
    layout="wide"
)

# 2. Premium Custom Theming & Typography
st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at 50% 50%, #0d1b2a, #1b263b, #0b0c10);
        color: #ffffff !important;
    }
    .launch-title {
        text-align: center;
        font-family: 'Arial Black', Gadget, sans-serif;
        font-size: 3rem !important;
        font-weight: 900;
        background: linear-gradient(90deg, #00f2fe, #4facfe, #ffcc00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 15px;
        margin-bottom: 0px;
    }
    .launch-subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #00f2fe !important;
        font-weight: bold;
        margin-bottom: 30px;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }
    .panel-box {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(0, 242, 254, 0.2);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
    }
    h2, h3, p, span, div {
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Dynamic Header Block
st.markdown('<h1 class="launch-title">GLOBALINTERNET.PY TAKING OFF</h1>', unsafe_allow_html=True)
st.markdown('<p class="launch-subtitle">🚀 The Symbolic Ascent of Elite Python Engineering 🚀</p>', unsafe_allow_html=True)

# 4. Interactive Simulation Matrix
col_left, col_right = st.columns([1, 2])

with col_left:
    st.markdown("### 🎛️ Flight Command Console")
    st.write("Control the symbolic trajectory variables of GlobalInternet.py as we disrupt the custom software market.")
    
    st.markdown('<div class="panel-box">', unsafe_allow_html=True)
    engine_thrust = st.slider("Engine Core Thrust (%)", min_value=0, max_value=100, value=85)
    climb_angle = st.slider("Pitch Ascent Angle (Degrees)", min_value=0, max_value=45, value=15)
    gear_status = st.radio("Landing Gear Status", ["Extended / Taxi", "Retracted / Cruise Flight"])
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("### 🏢 Mission Control Profile")
    st.markdown(
        """
        - **Captain & Chief Architect:** Gesner Deslandes
        - **Livery ID:** `GLOBALINTERNET.PY`
        - **Target Altitude:** Infinite Scalability
        - **Distribution Model:** Zero Subscriptions
        """
    )

with col_right:
    st.markdown("### 🌤️ Live Aerodynamic Vector Sandbox")
