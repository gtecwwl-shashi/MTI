import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="MTI Pathway Landscape", layout="wide")

st.markdown("### 📋 Full MTI Pathway – Trust-Level Visual Flow")

# Mermaid code using 'graph LR' with Subgraphs acting as Columns
mermaid_code = """
graph LR
    subgraph "1. Strategic & <br/> Programme Design"
        S1([Start]) --> S2[Strategic Intent]
        S2 --> S3[Programme Design]
        S3 --> S3a[Role Description]
        S3 --> S3b[Educational Objectives]
        S3 --> S3c[Duration / Exposure]
        S3c --> S4[Clinical Director]
    end

    subgraph "2. Governance & <br/> Candidate Sourcing"
        S4 --> G1[Governance:<br/>Stakeholders]
        G1 --> G2[/Trust Approval/]
        G2 --> G3[Sourcing:<br/>Partner / Sponsor]
    end

    subgraph "3. Pre-Arrival & <br/> Induction"
        G3 --> P1[GMC Registration]
        P1 --> P2[Visa Sponsorship]
        P2 --> P3[Pre-arrival:<br/>Welcome Pack]
    end

    subgraph "4. Training & <br/> Monitoring"
        P3 --> T1[Structured Training:<br/>Micro / Lab / MDT]
        T1 --> T2[Regular Supervision:<br/>ES/CS Meetings]
        T2 --> T3{Decision Points}
    end

    subgraph "5. Programme Exit & <br/> Improvement"
        T3 --> E1[Final Review]
        E1 --> E2[Return / Career]
        E2 --> E3[Outcomes & Feedback]
        E3 --> E4([End])
    end

    %% Styling Classes for High-Fidelity Colors
    classDef startEnd fill:#d4edda,stroke:#28a745,stroke-width:2px;
    classDef headerNode fill:#1a3a5f,color:#fff,font-weight:bold,stroke:#1a3a5f;
    classDef subNode fill:#e9ecef,stroke:#adb5bd,color:#333;
    
    %% Applying Classes
    class S1,E4 startEnd;
    class S2,G1,G3,P3,T1,E1 headerNode;
    class S3,S3a,S3b,S3c,S4,G2,P1,P2,T2,E2,E3 subNode;
"""

def render_mermaid(code):
    # Using a custom div with 'min-width' to ensure it fits in landscape without squishing
    html = f"""
    <div id="graph-container" style="display: flex; justify-content: center; width: 100%; overflow-x: auto;">
        <div class="mermaid" style="min-width: 1200px;">
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
                curve: 'linear',
                rankSpacing: 40,
                nodeSpacing: 20
            }},
            themeVariables: {{
                'primaryColor': '#ffffff',
                'edgeLabelBackground':'#ffffff',
                'tertiaryColor': '#f8f9fa'
            }}
        }});
    </script>
    """
    components.html(html, height=800, scrolling=True)

render_mermaid(mermaid_code)

st.caption("✨ Optimized for Landscape view. Use the scrollbar if viewing on a narrow screen.")
