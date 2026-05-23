import streamlit as st

# 1. Page Configuration Architecture (Enforces compact layout variables)
st.set_page_config(
    page_title="GlobalInternet.py | Flight Launch Engine",
    page_icon="✈️",
    layout="wide"
)

# 2. Ultra-Compact Premium Custom Theming
st.markdown(
    """
    <style>
    /* Force viewport compression and block scrolling artifacts */
    html, body, [data-testid="stAppViewContainer"] {
        max-height: 100vh !important;
        overflow: hidden !important;
    }
    .stApp {
        background: radial-gradient(circle at 50% 50%, #0d1b2a, #1b263b, #0b0c10);
        color: #ffffff !important;
    }
    /* Reduce top padding spacing buffers */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 0rem !important;
    }
    .launch-title {
        text-align: center;
        font-family: 'Arial Black', Gadget, sans-serif;
        font-size: 2.6rem !important;
        font-weight: 900;
        background: linear-gradient(90deg, #00f2fe, #4facfe, #ffcc00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 0px;
        margin-bottom: 2px;
    }
    .launch-subtitle {
        text-align: center;
        font-size: 1.05rem;
        color: #00f2fe !important;
        font-weight: bold;
        margin-bottom: 12px;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }
    .top-contact-bar {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(0, 242, 254, 0.3);
        border-radius: 10px;
        padding: 8px;
        margin-bottom: 15px;
        text-align: center;
        font-size: 0.95rem;
    }
    .top-link {
        color: #ffcc00 !important;
        font-weight: bold;
        text-decoration: none;
    }
    .top-link:hover {
        text-decoration: underline;
        color: #00f2fe !important;
    }
    .livery-text-display {
        font-size: 2.3rem;
        font-weight: bold;
        color: #ffcc00 !important;
        text-align: center;
        font-family: monospace;
        border: 2px dashed #00f2fe;
        padding: 8px;
        border-radius: 12px;
        background: rgba(0, 242, 254, 0.05);
        margin-bottom: 12px;
        letter-spacing: 2px;
    }
    /* Restrict the output height layout of the main photo matrix */
    [data-testid="stImage"] img {
        max-height: 45vh !important;
        object-fit: cover !important;
        border-radius: 12px;
    }
    h1, p, span, div {
        color: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Dynamic Header Block
st.markdown('<h1 class="launch-title">GLOBALINTERNET.PY TAKING OFF</h1>', unsafe_allow_html=True)
st.markdown('<p class="launch-subtitle">🚀 The Symbolic Ascent of Elite Python Engineering 🚀</p>', unsafe_allow_html=True)

# 4. Compact Top Contact Matrix Placement
st.markdown('<div class="top-contact-bar">', unsafe_allow_html=True)
col_c1, col_c2, col_c3 = st.columns(3)
with col_c1:
    st.markdown("📞 **Direct Comm Line:** (509) 4738-5663")
with col_c2:
    st.markdown("📧 **Secure Flight Deck Mail:** deslandes78@gmail.com")
with col_c3:
    st.markdown("🌐 **Main Command Base:** <a class='top-link' href='https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/' target='_blank'>Launch Live Hub ↗️</a>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 5. Compact Hull Branding Livery View
st.markdown('<div class="livery-text-display">✈️ Globalinternet.py</div>', unsafe_allow_html=True)

# 6. Constrained Aspect-Ratio Image Node
st.image(
    "https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcQpDNT5kAjY3ffixkFlbpnTJZyp-hHIuM5HFJH2g5EqIFAhQhzn-O85yT0D5Yi3fnGCUevaSOANBjExR3U",
    use_container_width=True
)
