import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="MTI Pathway Master", layout="wide")

st.markdown("## 🏛️ MTI Pathway – Trust-Level Visual Flow")
st.markdown("#### Infection Sciences Model")

def render_pillar(code, height=950):
    html = f"""
    <div style="background: #f0f7ff; border: 2px solid #005eb8; padding: 15px; border-radius: 10px; height: {height}px; overflow-y: auto;">
        <div class="mermaid">
            {code}
        </div>
    </div>
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ 
            startOnLoad: true, 
            theme: 'base',
            flowchart: {{ 
                useMaxWidth: false, 
                htmlLabels: true, 
                curve: 'basis',
                rankSpacing: 30,
                nodeSpacing: 10
            }},
            themeVariables: {{ 
                'fontSize': '15px', 
                'fontFamily': 'Arial',
                'primaryColor': '#ffffff',
                'lineColor': '#005eb8'
            }}
        }});
    </script>
    """
    components.html(html, height=height + 20)

# Styling definitions
styles = """
    classDef startEnd fill:#d4edda,stroke:#28a745,stroke-width:2px;
    classDef mainNode fill:#005eb8,color:#fff,font-weight:bold,stroke:#002f5c;
    classDef subNode fill:#ffffff,stroke:#005eb8,color:#002f5c;
    classDef logicNode fill:#002f5c,color:#fff,stroke:#002f5c;
"""

# --- ROW 1: STAGES 1 - 5 ---
row1 = st.columns(5)

with row1[0]:
    st.markdown("**1. Strategic Intent**")
    render_pillar(f"""graph TD
    A1([Start]) --> A2["Identify Workforce Gap /<br/>Training Opportunity"]
    A2 --> A3["Align with Trust Workforce<br/>+ Education Strategy"]
    A3 --> A4["Agreement in Principle<br/>(CD + Med Ed)"]
    {styles}
    class A1 startEnd; class A2,A4 mainNode; class A3 subNode;""")

with row1[1]:
    st.markdown("**2. Programme Design**")
    render_pillar(f"""graph TD
    B1["Define MTI Post(s)"] --> B2["• Role description<br/>• Educational objectives<br/>• Duration (12–24 months)"]
    B2 --> B3["Confirm Training Value"]
    B3 --> B4["• Hands-on lab exposure<br/>• Clinical microbiology<br/>• Teaching/QI"]
    B4 --> B5["Identify Supervisors<br/>• ES & CS"]
    {styles}
    class B1,B3 mainNode; class B2,B4,B5 subNode;""")

with row1[2]:
    st.markdown("**3. Governance**")
    render_pillar(f"""graph TD
    C1["Engage Stakeholders<br/>• Med Ed / HR / Finance"] --> C2["Royal College Route<br/>(e.g. RCPath)"]
    C2 --> C3[/"Trust Approval<br/>• Job plan validation<br/>• Induction capacity"/]
    C3 --> C4["Post Approved for MTI"]
    {styles}
    class C1,C4 mainNode; class C2,C3 subNode;""")

with row1[3]:
    st.markdown("**4. Candidate Pipeline**")
    render_pillar(f"""graph TD
    D1["Identify Int. Partner<br/>(e.g. Sri Lanka)"] --> D2["Candidate EOI"]
    D2 --> D3["Shortlisting & Interview"]
    D3 --> D4["RC Sponsorship<br/>Confirmation"]
    {styles}
    class D1,D4 mainNode; class D2,D3 subNode;""")

with row1[4]:
    st.markdown("**5. Pre-Arrival**")
    render_pillar(f"""graph TD
    E1["GMC Registration"] --> E2["Visa Sponsorship<br/>(Tier 5 – MTI route)"]
    E2 --> E3["Pre-arrival Engagement"]
    E3 --> E4["• Welcome pack<br/>• Role expectations<br/>• Induction plan"]
    {styles}
    class E1,E3 mainNode; class E2,E4 subNode;""")

st.markdown("---")

# --- ROW 2: STAGES 6 - 10 ---
row2 = st.columns(5)

with row2[0]:
    st.markdown("**6. Induction**")
    render_pillar(f"""graph TD
    F1["Trust Induction<br/>(HR + Mandatory)"] --> F2["Dept Induction<br/>• Lab systems<br/>• Clinical pathways"]
    F2 --> F3["Supernumerary Period"]
    F3 --> F4["Gradual Integration"]
    {styles}
    class F1,F4 mainNode; class F2,F3 subNode;""")

with row2[1]:
    st.markdown("**7. Training Delivery**")
    render_pillar(f"""graph TD
    G1["Structured Training<br/>• Clinical Micro<br/>• Lab / MDT"] --> G2["Regular Supervision<br/>• ES/CS meetings<br/>• Portfolio reviews"]
    G2 --> G3["Access to Teaching,<br/>QI & Leadership"]
    {styles}
    class G1 mainNode; class G2,G3 subNode;""")

with row2[2]:
    st.markdown("**8. Quality Assurance**")
    render_pillar(f"""graph TD
    H1["3 / 6 / 12 Month Reviews"] --> H2["Feedback Collection<br/>• Trainee / Supervisors"]
    H2 --> H3{{"Address Issues Early<br/>• Workload / Support"}}
    {styles}
    class H1 mainNode; class H2 subNode; class H3 logicNode;""")

with row2[3]:
    st.markdown("**9. Exit Planning**")
    render_pillar(f"""graph TD
    I1["Final Review & Sign-off"] --> I2["Support Return Home<br/>(or Career Guidance)"]
    I2 --> I3["Capture Outcomes<br/>& Feedback"]
    {styles}
    class I1 mainNode; class I2,I3 subNode;""")

with row2[4]:
    st.markdown("**10. Improvement**")
    render_pillar(f"""graph TD
    J1["Evaluate Programme"] --> J2["Refine Model"]
    J2 --> J3["Expand MTI Capacity"]
    J3 --> J4([End])
    {styles}
    class J1,J3 mainNode; class J2 subNode; class J4 startEnd;""")
