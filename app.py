import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="MTI Swimlane Dashboard", layout="wide")

st.markdown("### 📋 Full MTI Pathway – Infection Sciences Model")

# Using 'graph LR' for the columns, but 'direction TB' for the content inside columns
mermaid_code = """
graph LR
    subgraph "1. Strategic & <br/> Programme Design"
        direction TB
        S1([Start]) --> S2[Strategic Intent]
        S2 --> S3[Programme Design]
        S3 --> S3a[Role Description]
        S3a --> S3b[Educational Objectives]
        S3b --> S3c[Duration / Exposure]
        S3c --> S4[Clinical Director]
    end

    subgraph "2. Governance & <br/> Candidate Sourcing"
        direction TB
        G1[Governance:<br/>Stakeholders] --> G2[/Trust Approval/]
        G2 --> G3[Sourcing:<br/>Partner / Sponsor]
    end

    subgraph "3. Pre-Arrival & <br/> Induction"
        direction TB
        P1[GMC Registration] --> P2[Visa Sponsorship]
        P2 --> P3[Pre-arrival:<br/>Welcome Pack]
    end

    subgraph "4. Training & <br/> Monitoring"
        direction TB
        T1[Structured Training:<br/>Micro / Lab / MDT] --> T2[Regular Supervision:<br/>ES/CS Meetings]
        T2 --> T3{Decision Points}
    end

    subgraph "5. Programme Exit & <br/> Improvement"
        direction TB
        E1[Final Review] --> E2[Return / Career]
        E2 --> E3[Outcomes & Feedback]
        E3 --> E4([End])
    end

    %% Connections between the vertical swimlanes
    S4 --> G1
    G3 --> P1
    P3 --> T1
    T3 --> E1

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
    html = f"""
    <div style="display: flex; justify-content: center; width: 100%; padding: 10px;">
        <div class="mermaid" style="min-width: 1400px; border: 1px solid #ddd; padding: 20px; border-radius: 10px; background: white;">
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
                curve: 'basis'
            }},
            themeVariables: {{
                'primaryColor': '#ffffff',
                'edgeLabelBackground':'#ffffff',
                'tertiaryColor': '#f8f9fa',
                'fontSize': '14px'
            }}
        }});
    </script>
    """
    components.html(html, height=1000, scrolling=True)

render_mermaid(mermaid_code)
