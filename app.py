import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="MTI Pathway Pro", layout="wide")

st.title("Full MTI Pathway – Visual Flow")
st.write("Infection Sciences Model (High-Fidelity Re-creation)")

# Mermaid Code with custom class styles for colors
mermaid_code = """
graph TD
    %% Stage 1
    subgraph "1. Strategic & Programme Design"
        S1([Start]) --> S2[Strategic Intent]
        S2 --> S3[Programme Design]
        S3 --> S3a[Role Description]
        S3 --> S3b[Educational Objectives]
        S3 --> S3c[Duration / Hands-on Exposure]
        S3c --> S4[Clinical Director Approval]
    end

    %% Stage 2
    subgraph "2. Governance & Candidate Sourcing"
        S4 --> G1[Governance:<br/>Stakeholders / HR / Finance]
        G1 --> G2[/Trust Approval/]
        G2 --> G3[Governance & Candidate Sourcing:<br/>Identify Partner / RC Sponsor]
    end

    %% Stage 3
    subgraph "3. Pre-Arrival & Induction"
        G3 --> P1[GMC Registration Process]
        P1 --> P2[Visa Sponsorship Tier 5]
        P2 --> P3[Pre-arrival Engagement:<br/>Welcome Pack / Lab System]
    end

    %% Stage 4
    subgraph "4. Training & Monitoring"
        P3 --> T1[Structured Training Programme:<br/>Microbiology / Lab / MDT]
        T1 --> T2[Regular Supervision:<br/>ES/CS Meetings / Portfolio]
        T2 --> T3{Decision Points}
    end

    %% Stage 5
    subgraph "5. Programme Exit & Improvement"
        T3 --> E1[Final Review & Sign-off]
        E1 --> E2[Return to Home Country / Career Guidance]
        E2 --> E3[Capture Outcomes & Feedback]
        E3 --> E4([End])
    end

    %% Styling Classes (To match your image colors)
    classDef startEnd fill:#d4edda,stroke:#28a745,stroke-width:2px;
    classDef headerNode fill:#1a3a5f,color:#fff,font-weight:bold,stroke:#1a3a5f;
    classDef subNode fill:#e9ecef,stroke:#adb5bd,color:#333;
    classDef actionNode fill:#34495e,color:#fff,stroke:#2c3e50;

    %% Applying Classes
    class S1,E4 startEnd;
    class S2,G1,G3,P3,T1,E1 headerNode;
    class S3,S3a,S3b,S3c,S4,G2,P1,P2,T2,E2,E3 subNode;
"""

def render_mermaid(code):
    html = f"""
    <div class="mermaid" style="display: flex; justify-content: center; background-color: #ffffff; padding: 20px;">
        {code}
    </div>
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ 
            startOnLoad: true, 
            theme: 'base',
            themeVariables: {{
                'primaryColor': '#ffffff',
                'primaryTextColor': '#333',
                'primaryBorderColor': '#1a3a5f',
                'lineColor': '#1a3a5f',
                'secondaryColor': '#f8f9fa',
                'tertiaryColor': '#ffffff'
            }}
        }});
    </script>
    """
    components.html(html, height=1500, scrolling=True)

render_mermaid(mermaid_code)
