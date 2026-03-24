import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="MTI Pathway Vertical", layout="wide")

st.title("MTI Pathway – Vertical Visual Flow")
st.write("Trust-Level Infection Sciences Model")

# 'graph TD' creates the Vertical Flow
mermaid_code = """
graph TD
    subgraph "1. Strategic Intent & Programme Design"
        S1([Start]) --> S2[1.1 Identify Workforce Gap / Training Opportunity]
        S2 --> S3[1.2 Align with Trust Strategy]
        S3 --> S4[1.3 Clinical Director & Med Ed Approval]
    end

    subgraph "2. Governance & Design"
        S4 --> G1[2.1 Define MTI Posts<br/>- Role Description<br/>- Educational Objectives]
        G1 --> G2[2.2 Confirm Training Value<br/>- Lab Exposure<br/>- Clinical Micro]
        G2 --> G3[2.3 Identify Supervisors]
    end

    subgraph "3. Approvals & Sourcing"
        G3 --> A1[3.1 Engage Stakeholders<br/>- HR / Finance / Med Ed]
        A1 --> A2[3.2 Royal College Sponsorship<br/>- RCPath]
        A2 --> A3[/3.3 Trust Post Approval/]
    end

    subgraph "4. Candidate Pipeline & Pre-Arrival"
        A3 --> P1[4.1 Identify International Partner]
        P1 --> P2[4.2 Candidate Interview & Shortlisting]
        P2 --> P3[4.3 GMC Registration & Visa Tier 5]
    end

    subgraph "5. Induction & Training"
        P3 --> I1[5.1 Trust & Dept Induction]
        I1 --> I2[5.2 Supernumerary Period / Shadowing]
        I2 --> I3[5.3 Structured Training & Supervision]
    end

    subgraph "6. Quality & Exit"
        I3 --> Q1[6.1 3/6/12 Month Reviews]
        Q1 --> Q2[6.2 Final Sign-off & Exit Planning]
        Q2 --> Q3([End: Continuous Improvement])
    end

    %% Styling
    style S1 fill:#d4edda,stroke:#333
    style Q3 fill:#d4edda,stroke:#333
    style A3 fill:#fff,stroke:#333,stroke-width:2px
    style T3 fill:#3498db,color:#fff
    
    %% Color coding the stages
    classDef stage1 fill:#f9f9f9,stroke:#333;
    classDef stage2 fill:#ffffff,stroke:#333;
    class S1,S2,S3,S4 stage1;
    class G1,G2,G3 stage2;
"""

def render_mermaid(code):
    html = f"""
    <div class="mermaid" style="display: flex; justify-content: center;">
        {code}
    </div>
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ 
            startOnLoad: true, 
            theme: 'neutral',
            flowchart: {{ useMaxWidth: true, htmlLabels: true, curve: 'basis' }}
        }});
    </script>
    """
    components.html(html, height=1200, scrolling=True)

render_mermaid(mermaid_code)
