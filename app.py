import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="MTI Pathway Visualizer", layout="wide")

st.title("MTI Pathway – Trust-Level Visual Flow")
st.write("Visualizing the Infection Sciences Model")

# Define the Mermaid diagram string
# 'graph LR' creates the swimlanes from Left to Right
mermaid_code = """
graph LR
    subgraph "1. Strategic & Programme Design"
        S1([Start]) --> S2[Strategic Intent]
        S2 --> S3[Programme Design<br/>Role, Objectives, Duration]
        S3 --> S4[Clinical Director Approval]
    end

    subgraph "2. Governance & Sourcing"
        S4 --> G1[Stakeholder Engagement<br/>Med Ed, HR, Finance]
        G1 --> G2[/Trust Approval/]
        G2 --> G3[Identify Int. Partner<br/>& Royal College Sponsor]
    end

    subgraph "3. Pre-Arrival & Induction"
        G3 --> P1[GMC Registration]
        P1 --> P2[Visa Sponsorship<br/>Tier 5]
        P2 --> P3[Pre-arrival Engagement<br/>Induction Plan]
    end

    subgraph "4. Training & Monitoring"
        P3 --> T1[Structured Training<br/>Lab & MDT]
        T1 --> T2[Regular Supervision<br/>ES/CS Meetings]
        T2 --> T3{Feedback & Reviews}
    end

    subgraph "5. Exit & Improvement"
        T3 --> E1[Final Sign-off]
        E1 --> E2[Capture Outcomes]
        E2 --> E3([End])
    end

    %% Styling
    style S1 fill:#d4edda,stroke:#333
    style E3 fill:#d4edda,stroke:#333
    style S2 fill:#34495e,color:#fff
    style S3 fill:#34495e,color:#fff
    style G1 fill:#34495e,color:#fff
    style G3 fill:#34495e,color:#fff
    style T1 fill:#34495e,color:#fff
    style E1 fill:#34495e,color:#fff
    style T3 fill:#3498db,color:#fff
"""

# Function to render Mermaid
def render_mermaid(code):
    html = f"""
    <div class="mermaid">
        {code}
    </div>
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ startOnLoad: true, theme: 'neutral' }});
    </script>
    """
    components.html(html, height=800, scrolling=True)

render_mermaid(mermaid_code)

st.info("💡 This version uses Mermaid.js for maximum stability on Streamlit Cloud.")
