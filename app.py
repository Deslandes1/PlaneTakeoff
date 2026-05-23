import streamlit as st

# 1. Page Configuration Architecture
st.set_page_config(
    page_title="GlobalInternet.py | Flight Launch Engine",
    page_icon="✈️",
    layout="wide"
)

# 2. Premium Custom Theming & Typography Matrix
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
    .livery-text-display {
        font-size: 2.5rem;
        font-weight: bold;
        color: #ffcc00 !important;
        text-align: center;
        font-family: monospace;
        border: 2px dashed #00f2fe;
        padding: 10px;
        border-radius: 10px;
        background: rgba(0, 242, 254, 0.05);
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

# 4. Interactive Simulation Layout
col_left, col_right = st.columns([1, 1.2])

with col_left:
    st.markdown("### 🎛️ Flight Command Console")
    st.write("Control the trajectory variables of GlobalInternet.py as we disrupt the custom software market.")
    
    st.markdown('<div class="panel-box">', unsafe_allow_html=True)
    engine_thrust = st.slider("Engine Core Thrust (%)", min_value=0, max_value=100, value=95)
    climb_angle = st.slider("Pitch Ascent Angle (Degrees)", min_value=0, max_value=45, value=18)
    gear_status = st.radio("Landing Gear Status", ["Extended / Taxi", "Retracted / Cruise Flight"], index=1)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("### 🏢 Mission Control Profile")
    st.markdown(
        """
        - **Captain & Chief Architect:** Gesner Deslandes
        - **Target Altitude:** Infinite Scalability
        - **Distribution Model:** Zero Subscriptions
        """
    )

with col_right:
    st.markdown("### ✈️ Hull Hull Branding Livery View")
    # This renders the exact custom name block representing the side of the fuselage
    st.markdown('<div class="livery-text-display">✈️ Globalinternet.py</div>', unsafe_allow_html=True)
    st.write("")
    
    # Live image framework fallback inside the right layout node
    st.image(
        "https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcQpDNT5kAjY3ffixkFlbpnTJZyp-hHIuM5HFJH2g5EqIFAhQhzn-O85yT0D5Yi3fnGCUevaSOANBjExR3U",
        caption="Ascent Profile Vectors Loaded: GlobalInternet.py Climbing Out of Runway 12",
        use_container_width=True
    )

# 5. Core Contact Routing Footer Terminal
st.markdown("---")
col_f1, col_f2, col_f3 = st.columns(3)
with col_f1:
    st.markdown("📞 **Direct Comm Line:** (509) 4738-5663")
with col_f2:
    st.markdown("📧 **Secure Flight Deck Mail:** deslandes78@gmail.com")
with col_f3:
    st.markdown("🌐 **Main Command Base:** [Launch Live Hub ↗️](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
