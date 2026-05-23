import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="GlobalInternet.py | Radar Flight Command",
    page_icon="📡",
    layout="wide"
)

# 2. Premium Aviator Styling Sheet
st.markdown(
    """
    <style>
    .stApp {
        background: #060913 !important;
        color: #ffffff !important;
    }
    .radar-title {
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
        font-size: 2.8rem !important;
        color: #00ff66 !important;
        text-shadow: 0 0 15px rgba(0, 255, 102, 0.4);
        margin-top: 10px;
        margin-bottom: 0px;
    }
    .radar-subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #00f2fe !important;
        font-family: monospace;
        margin-bottom: 25px;
    }
    .instr-box {
        background: #0c1020;
        border: 2px solid #1e295d;
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 15px;
        font-family: monospace;
    }
    .green-glow {
        color: #00ff66;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Cockpit Header Array
st.markdown('<h1 class="radar-title">📡 FLIGHT RADAR & STEERING TERMINAL</h1>', unsafe_allow_html=True)
st.markdown('<p class="radar-subtitle">SYSTEM LOG: LIVERY TARGET [GLOBALINTERNET.PY] READY FOR INTERACTIVE DEPLOYMENT</p>', unsafe_allow_html=True)

# 4. Interface Split: Instrumentation vs. Flight Display
col_left, col_right = st.columns([1, 2.2])

with col_left:
    st.markdown("### 🎛️ Flight Deck Status")
    
    st.markdown('<div class="instr-box">', unsafe_allow_html=True)
    st.markdown("🌐 **AIRCRAFT CALLSIGN:** <span class='green-glow'>GlobalInternet.py</span>", unsafe_allow_html=True)
    st.markdown("⚙️ **PROPULSION:** Custom Built Python Core (Zero Subscriptions)", unsafe_allow_html=True)
    st.markdown("🎯 **MISSION TASK:** Take off anytime, scan radar matrix vectors, find ideal safe green zone runways, and land safely.", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### 🎮 Steering Wheel Instructions")
    st.markdown(
        """
        Click directly on the black Radar Canvas window to assign direct focus, then use your keyboard:
        * ⬆️ **Up Arrow:** Activate Thrusters / Pitch Nose Up (Take Off)
        * ⬅️ **Left Arrow:** Turn Flight Path Left
        * ➡️ **Right Arrow:** Turn Flight Path Right
        * ⬇️ **Down Arrow:** Air Brakes / Descent Vector Control
        """
    )
    
    # Quick utility fallback triggers for mobile screens
    st.write("")
    st.info("💡 **Developer Check:** Keep your engine thrust sustained high using the Up Arrow to break ground effect and clear safe obstacle altitudes.")

with col_right:
    st.markdown("### 📡 Live Tactical Screen Canvas Matrix")

    # Pure HTML5 / JavaScript integration logic injected directly into the frontend layout stream
    # This bypasses server-client latencies for fluid game-loop calculation ticks
    flight_simulator_html = """
    <div style="text-align: center;">
        <canvas id="flightRadarCanvas" width="750" height="480" style="border: 3px solid #1e295d; background: #02040a; border-radius: 8px; box-shadow: 0 0 20px rgba(0,242,254,0.1); font-family: monospace;"></canvas>
        <p style="color: #888888; font-size: 0.85rem; margin-top: 5px; font-family: monospace;">[ Click on viewport screen above before initializing Arrow keys ]</p>
    </div>

    <script>
    const canvas = document.getElementById('flightRadarCanvas');
    const ctx = canvas.getContext('2d');

    // Flight variables initialization
    let plane = {
        x: 100,
        y: 400,
        speed: 0,
        angle: 0,
        altitude: 0,
        isFlying: false,
        name: "GlobalInternet.py"
    };

    // Safe landing strip variables
    let safeZone = {
        x: 550,
        y: 120,
        radius: 40,
        name: "OPTIMAL LANDING BASIN (RUNWAY 01)"
    };

    let radarSweepAngle = 0;
    let keys = {};

    // Keyboard capture configuration
    window.addEventListener('keydown', function(e) {
        if([37, 38, 39, 40].indexOf(e.keyCode) > -1) {
            e.preventDefault(); // Disables default page scrolling artifacts
        }
        keys[e.keyCode] = true;
    }, false);

    window.addEventListener('keyup', function(e) {
        keys[e.keyCode] = false;
    }, false);

    function updateFlightSimulation() {
        // Steering control configuration mapping
        if (keys[38]) { // Up Arrow: Engine Thrust up / Take off climb
            plane.speed = Math.min(plane.speed + 0.12, 4.5);
            if(plane.speed > 1.8) {
                plane.isFlying = true;
                plane.altitude = Math.min(plane.altitude + 0.5, 100);
            }
        }
        if (keys[40]) { // Down Arrow: Reduce speed / Descend
            plane.speed = Math.max(plane.speed - 0.1, 0);
            if(plane.speed < 1.5) {
                plane.altitude = Math.max(plane.altitude - 0.8, 0);
                if(plane.altitude === 0) plane.isFlying = false;
            }
        }
        if (keys[37]) { // Left Arrow: Counter-Clockwise bank angle
            plane.angle -= 0.05;
        }
        if (keys[39]) { // Right Arrow: Clockwise bank angle
            plane.angle += 0.05;
        }

        // Apply spatial positional displacements based on angle math
        if (plane.speed > 0) {
            plane.x += Math.cos(plane.angle) * plane.speed;
            plane.y += Math.sin(plane.angle) * plane.speed;
        }

        // Boundary edge loops wrapping
        if (plane.x < 0) plane.x = canvas.width;
        if (plane.x > canvas.width) plane.x = 0;
        if (plane.y < 0) plane.y = canvas.height;
        if (plane.y > canvas.height) plane.y = 0;

        radarSweepAngle += 0.03;
    }

    function renderRadarCanvas() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw radar sweeping guidelines circles rings
        ctx.strokeStyle = "rgba(0, 255, 102, 0.15)";
        ctx.lineWidth = 1;
        for(let r = 100; r < canvas.width; r += 120) {
            ctx.beginPath();
            ctx.arc(canvas.width/2, canvas.height/2, r, 0, Math.PI*2);
            ctx.stroke();
        }

        // Radar scanning glowing needle sweep visualization
        ctx.strokeStyle = "rgba(0, 255, 102, 0.08)";
        ctx.beginPath();
        ctx.moveTo(canvas.width/2, canvas.height/2);
        ctx.lineTo(canvas.width/2 + Math.cos(radarSweepAngle)*800, canvas.height/2 + Math.sin(radarSweepAngle)*800);
        ctx.stroke();

        // Draw Safe Landing Zone Site flagged via target sweeps
        ctx.strokeStyle = "#00f2fe";
        ctx.fillStyle = "rgba(0, 242, 254, 0.1)";
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.arc(safeZone.x, safeZone.y, safeZone.radius, 0, Math.PI*2);
        ctx.fill();
        ctx.stroke();
        
        // Landing zone radar target text tag
        ctx.fillStyle = "#00f2fe";
        ctx.font = "10px monospace";
        ctx.fillText("📡 RADAR LOCK: SUITABLE LANDING HUB", safeZone.x - 80, safeZone.y - 48);

        // Calculate proximity metrics to judge landing success variables
        let dx = plane.x - safeZone.x;
        let dy = plane.y - safeZone.y;
        let distance = Math.sqrt(dx*dx + dy*dy);
        
        // Draw Plane (Represented by a sleek sleek dynamic directional polygon arrow)
        ctx.save();
        ctx.translate(plane.x, plane.y);
        ctx.rotate(plane.angle);
        
        // Fuselage Core Base
        ctx.fillStyle = plane.isFlying ? "#ffffff" : "#aaaaaa";
        ctx.beginPath();
        ctx.moveTo(18, 0);
        ctx.lineTo(-12, -7);
        ctx.lineTo(-12, 7);
        ctx.closePath();
        ctx.fill();

        // Wing expansions structures
        ctx.strokeStyle = "#4facfe";
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(-2, 0);
        ctx.lineTo(-6, -22);
        ctx.moveTo(-2, 0);
        ctx.lineTo(-6, 22);
        ctx.stroke();
        ctx.restore();

        // Overlay text label directly following right alongside the aircraft fuselage path
        ctx.fillStyle = "#ffcc00";
        ctx.font = "bold 11px monospace";
        ctx.fillText(plane.name, plane.x - 45, plane.y - 28);

        // On-screen HUD Telemetry Dashboard outputs overlay
        ctx.fillStyle = "rgba(2, 4, 10, 0.75)";
        ctx.fillRect(10, 10, 260, 95);
        ctx.strokeStyle = "#1e295d";
        ctx.strokeRect(10, 10, 260, 95);

        ctx.fillStyle = "#00ff66";
        ctx.font = "12px monospace";
        ctx.fillText("AIR SPEED: " + (plane.speed * 45).toFixed(0) + " KNOTS", 20, 30);
        ctx.fillText("ALTITUDE: " + (plane.altitude * 8).toFixed(0) + " FEET", 20, 50);
        ctx.fillText("FLIGHT CONFIG: " + (plane.isFlying ? "🚀 CLIMB OUT / CRUISE" : "💤 TAXIWAY GROUND"), 20, 70);
        
        if (distance < safeZone.radius) {
            if (!plane.isFlying && plane.speed === 0) {
                ctx.fillStyle = "#00ff66";
                ctx.fillText("🎉 TOUCHDOWN SUCCESSFUL! LOCKED!", 20, 90);
            } else {
                ctx.fillStyle = "#ffcc00";
                ctx.fillText("🚨 REDUCE SPEED & ALT TO LAND", 20, 90);
            }
        } else {
            ctx.fillStyle = "#ffffff";
            ctx.fillText("📡 RADAR RANGE OUT: SEEKING HUB", 20, 90);
        }
    }

    function flightLoopTick() {
        updateFlightSimulation();
        renderRadarCanvas();
        requestAnimationFrame(flightLoopTick);
    }

    // Initialize system execution loops
    flightLoopTick();
    </script>
    """
    st.components.v1.html(flight_simulator_html, height=520, scrolling=False)

# 5. Core Contact Routing Footer Terminal
st.markdown("---")
col_f1, col_f2, col_f3 = st.columns(3)
with col_f1:
    st.markdown("📞 **Direct Operations Desk:** (509) 4738-5663")
with col_f2:
    st.markdown("📧 **Flight Dispatch Mail:** deslandes78@gmail.com")
with col_f3:
    st.markdown("🌐 **Main Command Base:** [Launch Live Hub ↗️](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
