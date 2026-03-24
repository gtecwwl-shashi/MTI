import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="MTI Vertical Pillars", layout="wide")

st.markdown("### 📋 Full MTI Pathway – High-Fidelity Pillar Model")

# Using 'flowchart LR' but forcing verticality with '---' invisible links if needed
mermaid_code = """
flowchart LR
    subgraph P1 ["1. Strategic & <br/> Programme Design"]
        direction TB
        S1([Start]) --> S2[Strategic Intent]
        S2 --> S3[Programme Design]
        S3 --> S3a[Role Description]
        S3a --> S3b[Educational Objectives]
        S3b --> S3c[Duration / Exposure]
        S3c --> S4[Clinical Director]
    end

    subgraph P2 ["2. Governance & <br/> Candidate Sourcing"]
        direction TB
        G1[Governance:<br/>Stakeholders] --> G2[/Trust Approval/]
        G2 --> G3[Sourcing:<br/>Partner / Sponsor]
    end

    subgraph P3 ["3. Pre-Arrival & <br/> Induction"]
        direction TB
        R1[GMC Registration] --> R2[Visa Sponsorship]
        R2 --> R3[Pre-arrival:<br/>Welcome Pack]
    end

    subgraph P4 ["4. Training & <br/> Monitoring"]
        direction TB
        T1[Structured Training:<br/>Micro / Lab / MDT] --> T2[Regular Supervision:<br/>ES/CS Meetings]
        T2 --> T3{Decision Points}
    end

    subgraph P5 ["5. Programme Exit & <br/> Improvement"]
        direction TB
        E1[Final Review] --> E2[Return / Career]
        E2 --> E3[Outcomes & Feedback]
        E3 --> E4([End])
    end

    %% Bridges between the pillars - using 'stepAfter' style
    S4 --> G1
    G3 --> R1
    R3 --> T1
    T3 --> E1

    %% Styling Classes for Colors
    classDef startEnd fill:#d4edda,stroke:#28a745,stroke-width:2px;
    classDef headerNode fill:#1a3a5f,color:#fff,font-weight:bold;
    classDef subNode fill:#e9ecef,stroke:#adb5bd,color:#333;
    
    class S1,E4 startEnd;
    class S2,G1,R1,T1,E1 headerNode;
    class S3,S3a,S3b,S3c,S4,G2,R2,R3,T2,E2,E3 subNode;
    
    %% Backgrounds for columns
    style P1 fill:#f8f9fa,stroke:#1a3a5f
    style P2 fill:#ffffff,stroke:#1a3a5f
    style P3 fill:#f8f9fa,stroke:#1a3a5f
    style P4 fill:#ffffff,stroke:#1a3a5f
    style P5 fill:#f8f9fa,stroke:#1a3a5f
"""

def render_mermaid(code):
    # The key is 'min-width' on the internal div to force landscape orientation
    html = f"""
    <div style="width: 100%; overflow-x: auto;">
        <div class="mermaid" style="min-width: 1600px; display: flex; justify-content: center;">
            {code}
        </div>
    </div>
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ 
            startOnLoad: true, 
            theme: 'base',
            flowchart: {{ 
                useMaxWidth: false, 
                htmlLabels: true, 
                curve: 'stepAfter',
                rankSpacing: 80,
                nodeSpacing: 20
            }}
        }});
    </script>
    """
    components.html(html, height=1000, scrolling=True)

render_mermaid(mermaid_code)
