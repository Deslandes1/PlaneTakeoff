import streamlit as st

# 1. Page Configuration Architecture (Set to wide for massive visual impact)
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
        font-size: 3.5rem !important;
        font-weight: 900;
        background: linear-gradient(90deg, #00f2fe, #4facfe, #ffcc00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 15px;
        margin-bottom: 5px;
    }
    .launch-subtitle {
        text-align: center;
        font-size: 1.3rem;
        color: #00f2fe !important;
        font-weight: bold;
        margin-bottom: 25px;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }
    .top-contact-bar {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(0, 242, 254, 0.3);
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 35px;
        text-align: center;
    }
    .top-link {
        color: #ffcc00 !important;
        font-weight: bold;
        text-decoration: none;
        font-size: 1.1rem;
    }
    .top-link:hover {
        text-decoration: underline;
        color: #00f2fe !important;
    }
    .livery-text-display {
        font-size: 3.2rem;
        font-weight: bold;
        color: #ffcc00 !important;
        text-align: center;
        font-family: monospace;
        border: 3px dashed #00f2fe;
        padding: 15px;
        border-radius: 15px;
        background: rgba(0, 242, 254, 0.05);
        margin-bottom: 20px;
        letter-spacing: 2px;
        box-shadow: 0 0 20px rgba(0, 242, 254, 0.1);
    }
    h1, h2, h3, p, span, div {
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Dynamic Header Block
st.markdown('<h1 class="launch-title">GLOBALINTERNET.PY TAKING OFF</h1>', unsafe_allow_html=True)
st.markdown('<p class="launch-subtitle">🚀 The Symbolic Ascent of Elite Python Engineering 🚀</p>', unsafe_allow_html=True)

# 4. Premium Top Contact Matrix Placement
st.markdown('<div class="top-contact-bar">', unsafe_allow_html=True)
col_c1, col_c2, col_c3 = st.columns(3)
with col_c1:
    st.markdown("📞 **Direct Comm Line:** (509) 4738-5663")
with col_c2:
    st.markdown("📧 **Secure Flight Deck Mail:** deslandes78@gmail.com")
with col_c3:
    st.markdown("🌐 **Main Command Base:** <a class='top-link' href='https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/' target='_blank'>Launch Live Hub ↗️</a>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 5. Full-Width Enlarged Aircraft Hull Presentation Layout
st.markdown('<div class="livery-text-display">✈️ Globalinternet.py</div>', unsafe_allow_html=True)

# Expanded cinema aspect-ratio image node covering the layout center
st.image(
    "https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcQpDNT5kAjY3ffixkFlbpnTJZyp-hHIuM5HFJH2g5EqIFAhQhzn-O85yT0D5Yi3fnGCUevaSOANBjExR3U",
    caption="Ascent Profile Vectors Loaded: GlobalInternet.py Climbing Into Infinite Scalability",
    use_container_width=True
)

# 6. Clean System Footer
st.markdown("<br><hr style='border-color: rgba(255,255,255,0.1);'>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; color: #666666; font-size: 0.9rem;'>GlobalInternet.py Aerospace Platform • Zero Subscriptions Engine</div>", unsafe_allow_html=True)
