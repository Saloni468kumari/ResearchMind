import streamlit as st
import time

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ResearchMind",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Responsive CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

/* ── Base ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}
.stApp {
    background: #1A1A1A;
    color: #F0F0F0;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #242424 !important;
    border-right: 1px solid #2E2E2E !important;
    min-width: 240px !important;
    max-width: 320px !important;
}
[data-testid="stSidebar"] * { color: #F0F0F0 !important; }

/* ── Sidebar collapse on small screens ── */
@media (max-width: 768px) {
    [data-testid="stSidebar"] {
        min-width: 100% !important;
        max-width: 100% !important;
    }
    [data-testid="stSidebarNav"] { display: none; }
    section[data-testid="stSidebar"] > div {
        padding: 12px !important;
    }
}

/* ── Typography ── */
h1, h2, h3 { font-family: 'JetBrains Mono', monospace !important; }

/* ── Run button ── */
.stButton > button {
    background: linear-gradient(135deg, #FF6B00, #FF9500) !important;
    color: #000000 !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 700 !important;
    font-size: 14px !important;
    padding: 10px 24px !important;
    width: 100% !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 4px 24px rgba(255,107,0,0.35) !important;
    letter-spacing: 0.04em !important;
    white-space: nowrap !important;
}
.stButton > button:hover {
    box-shadow: 0 8px 36px rgba(255,107,0,0.55) !important;
    transform: translateY(-1px) !important;
}

/* ── Text area ── */
.stTextArea textarea {
    background: #2E2E2E !important;
    border: 1.5px solid #3A3A3A !important;
    border-radius: 10px !important;
    color: #F0F0F0 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 13px !important;
    width: 100% !important;
}
.stTextArea textarea:focus {
    border-color: #FF6B00 !important;
    box-shadow: 0 0 0 3px rgba(255,107,0,0.15) !important;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: #242424 !important;
    border-bottom: 1px solid #2E2E2E !important;
    gap: 2px !important;
    flex-wrap: wrap !important;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: #555555 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 11px !important;
    font-weight: 600 !important;
    border-radius: 8px 8px 0 0 !important;
    padding: 8px 12px !important;
    white-space: nowrap !important;
}
.stTabs [aria-selected="true"] {
    background: rgba(255,107,0,0.1) !important;
    color: #FF6B00 !important;
    border-bottom: 2px solid #FF6B00 !important;
}

/* ── Code blocks ── */
.stCode, code {
    background: #2E2E2E !important;
    color: #FF9500 !important;
    border: 1px solid #3A3A3A !important;
    border-radius: 8px !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 11px !important;
    word-break: break-all !important;
}

/* ── Spinner ── */
.stSpinner > div { border-top-color: #FF6B00 !important; }

/* ── Alerts ── */
.stAlert { border-radius: 10px !important; }

/* ── Divider ── */
hr { border-color: #2E2E2E !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: #1A1A1A; }
::-webkit-scrollbar-thumb { background: #3A3A3A; border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: #4A4A4A; }

/* ── Mono label ── */
.mono-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #FF6B00;
    margin-bottom: 8px;
}

/* ── Responsive columns ── */
@media (max-width: 640px) {
    [data-testid="column"] {
        min-width: 45% !important;
        flex: 1 1 45% !important;
    }
}

/* ── Output box ── */
.output-box {
    background: #242424;
    border: 1px solid #2E2E2E;
    border-radius: 10px;
    padding: 20px 22px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: #C8C8C8;
    line-height: 1.8;
    white-space: pre-wrap;
    word-break: break-word;
    overflow-y: auto;
    max-height: 460px;
}

/* ── Agent card ── */
.agent-card {
    border-radius: 14px;
    padding: 12px 14px;
    margin-bottom: 8px;
    transition: all 0.4s ease;
}

/* ── Main header responsive ── */
.main-header {
    padding: 20px 0 14px;
}
.main-header-title {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 700;
    font-size: clamp(16px, 3vw, 24px);
    color: #F0F0F0;
    letter-spacing: 0.02em;
}
.main-header-sub {
    font-size: clamp(10px, 1.5vw, 13px);
    color: #555555;
    margin-top: 3px;
}

/* ── Metric card responsive ── */
.metric-card {
    background: #242424;
    border-radius: 14px;
    padding: clamp(10px, 2vw, 16px);
    transition: all 0.4s;
    height: 100%;
}
.metric-icon { font-size: clamp(18px, 3vw, 22px); }
.metric-label {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600;
    font-size: clamp(10px, 1.5vw, 12px);
    margin-top: 8px;
}
.metric-badge {
    font-size: clamp(9px, 1.2vw, 11px);
    margin-top: 4px;
}
</style>
""", unsafe_allow_html=True)

# ── Import pipeline ────────────────────────────────────────────────────────────
try:
    from pipeline import run_research_pipeline
    PIPELINE_AVAILABLE = True
except ImportError:
    PIPELINE_AVAILABLE = False

# ── Session state ──────────────────────────────────────────────────────────────
for key, default in {
    "search_results": "",
    "scraped_content": "",
    "report": "",
    "feedback": "",
    "stage": "idle",
    "log": [],
    "error_msg": "",
    "error_at": "",
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# ── Stages ────────────────────────────────────────────────────────────────────
STAGES = [
    ("search", "🔍", "Search Agent",  "Scanning the web for reliable sources",  "#FF6B00"),
    ("reader", "📄", "Reader Agent",  "Scraping & extracting deep content",      "#FF9500"),
    ("writer", "✍️", "Writer Chain",  "Drafting comprehensive report",           "#FFB700"),
    ("critic", "🧐", "Critic Chain",  "Reviewing & providing feedback",          "#FF4500"),
]

def add_log(msg):
    ts = time.strftime("%H:%M:%S")
    st.session_state.log.append(f"[{ts}] {msg}")

def stage_status(stage_id):
    order   = ["search","reader","writer","critic"]
    current = st.session_state.stage
    if current == "done":  return "done"
    if current == "error":
        ci = order.index(st.session_state.error_at) if st.session_state.error_at in order else -1
        return "done" if order.index(stage_id) < ci else "idle"
    if current == "idle":  return "idle"
    ci = order.index(current) if current in order else -1
    si = order.index(stage_id)
    if si < ci:  return "done"
    if si == ci: return "running"
    return "idle"

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:

    # Logo + name
    st.markdown("""
    <div style='display:flex;align-items:center;gap:10px;margin-bottom:20px'>
      <div style='width:40px;height:40px;border-radius:12px;flex-shrink:0;
                  background:linear-gradient(135deg,#FF6B00,#FF9500);
                  display:flex;align-items:center;justify-content:center;
                  font-size:20px;box-shadow:0 0 20px rgba(255,107,0,0.4)'>🔬</div>
      <div style='min-width:0'>
        <div style='font-family:"JetBrains Mono",monospace;font-weight:700;
                    font-size:14px;color:#F0F0F0;white-space:nowrap;
                    overflow:hidden;text-overflow:ellipsis'>ResearchMind</div>
        <div style='font-size:10px;color:#555555;margin-top:1px'>Powered by Claude AI · 4 Agents</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="mono-label">Research Topic</div>', unsafe_allow_html=True)
    topic = st.text_area(
        label="topic",
        label_visibility="collapsed",
        placeholder="e.g. Quantum computing in 2025...",
        height=90,
        key="topic_input",
    )

    run_clicked = st.button("▶  Run Pipeline", use_container_width=True)

    st.markdown("<hr style='margin:16px 0'>", unsafe_allow_html=True)

    # Agent pipeline nodes
    st.markdown('<div class="mono-label" style="margin-bottom:10px">Agent Pipeline</div>',
                unsafe_allow_html=True)

    for i, (sid, icon, label, desc, color) in enumerate(STAGES):
        status  = stage_status(sid)
        border  = color + "80" if status == "done" else (color + "50" if status == "running" else "#3A3A3A")
        bg      = f"linear-gradient(135deg,{color}18,#242424)" if status in ("done","running") else "#2E2E2E"
        dot     = "✓" if status == "done" else ("●" if status == "running" else "○")
        dot_col = color if status != "idle" else "#444444"
        glow    = f"0 0 16px {color}35" if status == "running" else "none"

        st.markdown(f"""
        <div style='background:{bg};border:1.5px solid {border};border-radius:12px;
                    padding:11px 13px;margin-bottom:6px;box-shadow:{glow};
                    transition:all 0.4s ease'>
          <div style='display:flex;align-items:center;gap:10px'>
            <span style='font-size:18px;flex-shrink:0'>{icon}</span>
            <div style='flex:1;min-width:0'>
              <div style='font-family:"JetBrains Mono",monospace;font-weight:600;
                          font-size:11px;color:{color if status!="idle" else "#555555"};
                          white-space:nowrap;overflow:hidden;text-overflow:ellipsis'>
                Step {i+1} — {label}
              </div>
              <div style='font-size:10px;color:#444444;margin-top:2px;
                          white-space:nowrap;overflow:hidden;text-overflow:ellipsis'>{desc}</div>
            </div>
            <span style='color:{dot_col};font-size:13px;flex-shrink:0'>{dot}</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

        if i < len(STAGES) - 1:
            lit = status == "done"
            nc  = STAGES[i+1][4]
            st.markdown(f"""
            <div style='width:2px;height:12px;margin:0 0 6px 19px;
                        background:{"linear-gradient(to bottom,"+color+","+nc+")" if lit else "#3A3A3A"};
                        border-radius:2px'></div>
            """, unsafe_allow_html=True)

    st.markdown("<hr style='margin:14px 0'>", unsafe_allow_html=True)

    # Live log
    st.markdown('<div class="mono-label" style="margin-bottom:6px">Live Log</div>',
                unsafe_allow_html=True)
    log_text = "\n".join(st.session_state.log[-15:]) if st.session_state.log else "_"
    st.code(log_text, language=None)

    if st.session_state.stage == "done":
        st.success("✓ Pipeline complete — all 4 agents finished!")
    if st.session_state.error_msg:
        st.error(f"✕ {st.session_state.error_msg}")

# ── MAIN AREA ─────────────────────────────────────────────────────────────────

# Header
st.markdown("""
<div class="main-header">
  <div style='display:flex;align-items:center;gap:12px;flex-wrap:wrap'>
    <div style='width:44px;height:44px;border-radius:12px;flex-shrink:0;
                background:linear-gradient(135deg,#FF6B00,#FF9500);
                display:flex;align-items:center;justify-content:center;
                font-size:22px;box-shadow:0 0 24px rgba(255,107,0,0.4)'>🔬</div>
    <div>
      <div class="main-header-title">ResearchMind</div>
      <div class="main-header-sub">AI-Powered Multi-Agent Research System</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# Agent metric cards — 4 cols on large, 2x2 on small
col1, col2, col3, col4 = st.columns(4)
for col, (sid, icon, label, _, color) in zip([col1,col2,col3,col4], STAGES):
    s         = stage_status(sid)
    badge     = "✓ Done" if s=="done" else ("⏳ Running" if s=="running" else "— Idle")
    badge_col = "#4ADE80" if s=="done" else (color if s=="running" else "#444444")
    border    = color+"60" if s!="idle" else "#2E2E2E"
    glow      = f"0 0 16px {color}25" if s=="running" else "none"
    with col:
        st.markdown(f"""
        <div class="metric-card" style='border:1.5px solid {border};box-shadow:{glow}'>
          <div class="metric-icon">{icon}</div>
          <div class="metric-label" style='color:{color if s!="idle" else "#555555"}'>{label}</div>
          <div class="metric-badge" style='color:{badge_col}'>{badge}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<div style='height:18px'></div>", unsafe_allow_html=True)

# Output tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🔍 Search Results",
    "📄 Scraped Content",
    "✍️ Final Report",
    "🧐 Critic Feedback",
])

def render_output(content, placeholder, color):
    if content:
        st.markdown(f"""
        <div class="output-box" style='border-left:3px solid {color}'>
{content}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style='background:#242424;border:1px solid #2E2E2E;border-radius:10px;
                    padding:50px 20px;text-align:center;min-height:200px'>
          <div style='font-size:32px;opacity:0.15'>⏳</div>
          <div style='font-family:"JetBrains Mono",monospace;font-size:12px;
                      color:#3A3A3A;margin-top:10px'>{placeholder}</div>
        </div>
        """, unsafe_allow_html=True)

with tab1: render_output(st.session_state.search_results,  "Awaiting search results...",   "#FF6B00")
with tab2: render_output(st.session_state.scraped_content, "Awaiting scraped content...",  "#FF9500")
with tab3: render_output(st.session_state.report,          "Awaiting report...",           "#FFB700")
with tab4: render_output(st.session_state.feedback,        "Awaiting critic feedback...",  "#FF4500")

# ── Pipeline runner ────────────────────────────────────────────────────────────
if run_clicked:
    if not topic.strip():
        st.warning("Please enter a research topic in the sidebar.")
    elif not PIPELINE_AVAILABLE:
        st.error("⚠️ `pipeline.py` not found. Make sure `app.py` is in the same folder.")
    else:
        st.session_state.update({
            "search_results":"","scraped_content":"",
            "report":"","feedback":"",
            "log":[],"error_msg":"","error_at":"",
            "stage":"search",
        })
        add_log("Search agent activated — finding reliable sources...")
        st.rerun()

if st.session_state.stage in ("search","reader","writer","critic") and PIPELINE_AVAILABLE:
    stage     = st.session_state.stage
    topic_val = st.session_state.get("topic_input","")
    if not topic_val:
        st.session_state.stage = "idle"
        st.rerun()
    try:
        from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

        if stage == "search":
            with st.spinner("🔍 Search Agent scanning the web..."):
                agent  = build_search_agent()
                result = agent.invoke({"messages":[("user",
                    f"Find recent, reliable and detailed information about: {topic_val}")]})
                st.session_state.search_results = result["messages"][-1].content
                add_log("Search complete ✓")
                st.session_state.stage = "reader"
                add_log("Reader agent activated — scraping top resources...")

        elif stage == "reader":
            with st.spinner("📄 Reader Agent scraping top resources..."):
                agent  = build_reader_agent()
                result = agent.invoke({"messages":[("user",
                    f"Based on the following search results about '{topic_val}', "
                    f"pick the most relevant URL and scrape it for deeper content.\n\n"
                    f"Search Results:\n{st.session_state.search_results[:800]}")]})
                st.session_state.scraped_content = result["messages"][-1].content
                add_log("Scraping complete ✓")
                st.session_state.stage = "writer"
                add_log("Writer chain activated — drafting report...")

        elif stage == "writer":
            with st.spinner("✍️ Writer Chain drafting the report..."):
                combined = (f"SEARCH RESULTS:\n{st.session_state.search_results}\n\n"
                            f"DETAILED SCRAPED CONTENT:\n{st.session_state.scraped_content}")
                st.session_state.report = writer_chain.invoke(
                    {"topic": topic_val, "research": combined})
                add_log("Report drafted ✓")
                st.session_state.stage = "critic"
                add_log("Critic chain activated — reviewing report...")

        elif stage == "critic":
            with st.spinner("🧐 Critic Chain reviewing the report..."):
                st.session_state.feedback = critic_chain.invoke(
                    {"report": st.session_state.report})
                add_log("Review complete ✓")
                add_log("🎉 Pipeline completed successfully!")
                st.session_state.stage = "done"

    except Exception as e:
        st.session_state.error_msg = str(e)
        st.session_state.error_at  = stage
        st.session_state.stage     = "error"
        add_log(f"❌ Error: {e}")

    st.rerun()