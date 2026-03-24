import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="MTI Master Pathway", layout="wide")

st.markdown("### 🏛️ Full MTI Pathway – Trust-Level Visual Flow (Infection Sciences Model)")
st.markdown("---")

def render_pillar(code, height=600):
    html = f"""
    <div style="background: white; border: 1px solid #1a3a5f; padding: 10px; border-radius: 8px; height: {height}px; overflow-y: auto;">
        <div class="mermaid">
            {code}
        </div>
    </div>
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ 
            startOnLoad: true, 
            theme: 'base',
            flowchart: {{ useMaxWidth: true, htmlLabels: true, curve: 'basis' }},
            themeVariables: {{ 'fontSize': '13px', 'fontFamily': 'Arial' }}
        }});
    </script>
    """
    components.html(html, height=height + 20)

# --- ROW 1: Stages 1 to 5 ---
row1_cols = st.columns(5)

with row1_cols[0]:
    st.markdown("**1. Strategic Intent**")
    render_pillar("""
    graph TD
        A1([Start]) --> A2[Identify Workforce Gap]
        A2 --> A3[Align with Trust Strategy]
        A3 --> A4[Clinical Dir + Med Ed Approval]
        style A1 fill:#d4edda,stroke:#28a745
        style A2 fill:#1a3a5f,color:#fff
        style A4 fill:#34495e,color:#fff
    """)

with row1_cols[1]:
    st.markdown("**2. Programme Design**")
    render_pillar("""
    graph TD
        B1[Define MTI Posts<br/>- Role description<br/>- Educational objectives<br/>- Duration 12-24m]
        B1 --> B2[Confirm Training Value<br/>- Lab exposure<br/>- Clinical Micro<br/>- Teaching/QI]
        B2 --> B3[Identify Supervisors<br/>- Educational (ES)<br/>- Clinical (CS)]
        style B1 fill:#1a3a5f,color:#fff
        style B2 fill:#e9ecef
        style B3 fill:#e9ecef
    """)

with row1_cols[2]:
    st.markdown("**3. Governance**")
    render_pillar("""
    graph TD
        C1[Engage Stakeholders<br/>- Med Ed / HR / Finance]
        C1 --> C2[RC Sponsorship Route<br/>- e.g. RCPath]
        C2 --> C3[/Trust Approval/<br/>- Job plan validation<br/>- Induction capacity]
        C3 --> C4[Post Approved for MTI]
        style C1 fill:#1a3a5f,color:#fff
        style C3 fill:#e9ecef
    """)

with row1_cols[3]:
    st.markdown("**4. Candidate Pipeline**")
    render_pillar("""
    graph TD
        D1[Identify Int. Partner<br/>- e.g. Sri Lanka]
        D1 --> D2[Candidate EOI]
        D2 --> D3[Shortlist & Interview]
        D3 --> D4[RC Sponsorship Confirmation]
        style D1 fill:#1a3a5f,color:#fff
    """)

with row1_cols[4]:
    st.markdown("**5. Pre-Arrival**")
    render_pillar("""
    graph TD
        E1[GMC Registration Process]
        E1 --> E2[Visa Sponsorship<br/>- Tier 5 MTI Route]
        E2 --> E3[Pre-arrival Engagement<br/>- Welcome pack<br/>- Expectations<br/>- Induction plan]
        style E1 fill:#1a3a5f,color:#fff
        style E3 fill:#e9ecef
    """)

st.markdown("---")

# --- ROW 2: Stages 6 to 10 ---
row2_cols = st.columns(5)

with row2_cols[0]:
    st.markdown("**6. Induction & Transition**")
    render_pillar("""
    graph TD
        F1[Trust Induction<br/>- HR / Mandatory]
        F1 --> F2[Dept Induction<br/>- Lab systems<br/>- Pathways]
        F2 --> F3[Supernumerary Shadowing]
        F3 --> F4[Gradual Integration]
        style F1 fill:#1a3a5f,color:#fff
    """)

with row2_cols[1]:
    st.markdown("**7. Training Delivery**")
    render_pillar("""
    graph TD
        G1[Structured Training<br/>- Micro / Lab / MDT]
        G1 --> G2[Regular Supervision<br/>- ES/CS meetings<br/>- Portfolios]
        G2 --> G3[Access to Teaching,<br/>QI & Leadership]
        style G1 fill:#1a3a5f,color:#fff
        style G2 fill:#e9ecef
    """)

with row2_cols[2]:
    st.markdown("**8. Quality Assurance**")
    render_pillar("""
    graph TD
        H1[3/6/12 Month Reviews]
        H1 --> H2[Feedback Collection<br/>- Trainee / ES / CS]
        H2 --> H3{Address Issues Early<br/>- Workload / Support}
        style H1 fill:#1a3a5f,color:#fff
        style H3 fill:#3498db,color:#fff
    """)

with row2_cols[3]:
    st.markdown("**9. Exit Planning**")
    render_pillar("""
    graph TD
        I1[Final Review & Sign-off]
        I1 --> I2[Support Return Home<br/>- Career Guidance]
        I2 --> I3[Capture Outcomes]
        style I1 fill:#1a3a5f,color:#fff
    """)

with row2_cols[4]:
    st.markdown("**10. Improvement Loop**")
    render_pillar("""
    graph TD
        J1[Evaluate Programme]
        J1 --> J2[Refine Model]
        J2 --> J3[Expand Capacity]
        J3 --> J4([End / New Cohort])
        style J1 fill:#1a3a5f,color:#fff
        style J4 fill:#d4edda,stroke:#28a745
    """)
