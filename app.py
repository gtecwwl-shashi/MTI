import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="MTI Vertical Pillars", layout="wide")

st.markdown("### 📋 Full MTI Pathway – Trust-Level Visual Flow")
st.markdown("---")

# Helper function to render each pillar individually
def render_pillar(code, height=900):
    html = f"""
    <div style="background: white; border: 1px solid #ddd; padding: 10px; border-radius: 8px;">
        <div class="mermaid">
            {code}
        </div>
    </div>
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ 
            startOnLoad: true, 
            theme: 'base',
            flowchart: {{ useMaxWidth: true, htmlLabels: true, curve: 'basis' }}
        }});
    </script>
    """
    components.html(html, height=height)

# Create 5 Columns
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("**1. Strategic Design**")
    render_pillar("""
    graph TD
        S1([Start]) --> S2[Strategic Intent]
        S2 --> S3[Programme Design]
        S3 --> S3a[Role Description]
        S3a --> S3b[Educational Objectives]
        S3b --> S3c[Duration / Exposure]
        S3c --> S4[Clinical Director]
        style S1 fill:#d4edda,stroke:#28a745
        style S2 fill:#1a3a5f,color:#fff
    """)

with col2:
    st.markdown("**2. Governance**")
    render_pillar("""
    graph TD
        G1[Stakeholders / HR] --> G2[/Trust Approval/]
        G2 --> G3[Identify Partner]
        G3 --> G4[RC Sponsor]
        style G1 fill:#1a3a5f,color:#fff
        style G2 fill:#e9ecef
    """)

with col3:
    st.markdown("**3. Pre-Arrival**")
    render_pillar("""
    graph TD
        P1[GMC Registration] --> P2[Visa Tier 5]
        P2 --> P3[Welcome Pack]
        P3 --> P4[Induction Plan]
        style P1 fill:#1a3a5f,color:#fff
        style P2 fill:#e9ecef
    """)

with col4:
    st.markdown("**4. Training**")
    render_pillar("""
    graph TD
        T1[Micro / Lab / MDT] --> T2[ES/CS Meetings]
        T2 --> T3[Portfolio Review]
        T3 --> T4{Decision Point}
        style T1 fill:#1a3a5f,color:#fff
        style T4 fill:#3498db,color:#fff
    """)

with col5:
    st.markdown("**5. Exit & Review**")
    render_pillar("""
    graph TD
        E1[Final Review] --> E2[Return / Career]
        E2 --> E3[Capture Feedback]
        E3 --> E4([End])
        style E1 fill:#1a3a5f,color:#fff
        style E4 fill:#d4edda,stroke:#28a745
    """)

st.info("💡 Each column above is a vertical 'Pillar' of the MTI process.")
