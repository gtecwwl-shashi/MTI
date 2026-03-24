import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="MTI NHS Master Pathway", layout="wide")

# --- HEADER SECTION ---
st.markdown("## 🏛️ MTI Pathway Master Flow")
st.markdown("#### Infection Sciences Model (Trust-Level Visual Flow)")

def render_pillar(code, height=720):
    html = f"""
    <div style="background: #f0f7ff; border: 2px solid #005eb8; padding: 10px; border-radius: 10px; height: {height}px; overflow-y: auto;">
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
                useMaxWidth: true, 
                htmlLabels: true, 
                curve: 'basis',
                rankSpacing: 25,
                nodeSpacing: 10
            }},
            themeVariables: {{ 
                'fontSize': '16px', 
                'fontFamily': 'Arial',
                'primaryColor': '#ffffff',
                'lineColor': '#005eb8'
            }}
        }});
    </script>
    """
    components.html(html, height=height + 20)

# --- STYLING DEFINITIONS ---
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
    render_pillar(f"graph TD\nA1([Start]) --> A2['Identify Gap']\nA2 --> A3['Align Strategy']\nA3 --> A4['CD Approval']\n{styles}\nclass A1 startEnd; class A2,A4 mainNode; class A3 subNode;")
with row1[1]:
    st.markdown("**2. Programme Design**")
    render_pillar(f"graph TD\nB1['Define Posts<br/>• Role desc<br/>• Objectives']\nB1 --> B2['Training Value']\nB2 --> B3['ES & CS']\n{styles}\nclass B1 mainNode; class B2,B3 subNode;")
with row1[2]:
    st.markdown("**3. Governance**")
    render_pillar(f"graph TD\nC1['Stakeholders']\nC1 --> C2['RC Route']\nC2 --> C3[/'Trust Approval/']\nC3 --> C4['Post Approved']\n{styles}\nclass C1,C4 mainNode; class C2,C3 subNode;")
with row1[3]:
    st.markdown("**4. Candidate Pipeline**")
    render_pillar(f"graph TD\nD1['Identify Partner']\nD1 --> D2['EOI']\nD2 --> D3['Interview']\nD3 --> D4['RC Confirm']\n{styles}\nclass D1,D4 mainNode; class D2,D3 subNode;")
with row1[4]:
    st.markdown("**5. Pre-Arrival**")
    render_pillar(f"graph TD\nE1['GMC Process']\nE1 --> E2['Visa Tier 5']\nE2 --> E3['Welcome Pack']\n{styles}\nclass E1 mainNode; class E2,E3 subNode;")

st.markdown("---")

# --- ROW 2: STAGES 6 - 10 ---
row2 = st.columns(5)
with row2[0]:
    st.markdown("**6. Induction**")
    render_pillar(f"graph TD\nF1['Trust Induct']\nF1 --> F2['Dept Induct']\nF2 --> F3['Shadowing']\nF3 --> F4['Integration']\n{styles}\nclass F1,F4 mainNode; class F2,F3 subNode;")
with row2[1]:
    st.markdown("**7. Training Delivery**")
    render_pillar(f"graph TD\nG1['Training Plan']\nG1 --> G2['ES/CS Meetings']\nG2 --> G3['QI Projects']\n{styles}\nclass G1 mainNode; class G2,G3 subNode;")
with row2[2]:
    st.markdown("**8. Quality Assurance**")
    render_pillar(f"graph TD\nH1['Reviews']\nH1 --> H2['Feedback']\nH2 --> H3{{'Issues'}}\n{styles}\nclass H1 mainNode; class H2 subNode; class H3 logicNode;")
with row2[3]:
    st.markdown("**9. Exit Planning**")
    render_pillar(f"graph TD\nI1['Sign-off']\nI1 --> I2['Return Support']\nI2 --> I3['Outcomes']\n{styles}\nclass I1 mainNode; class I2,I3 subNode;")
with row2[4]:
    st.markdown("**10. Improvement**")
    render_pillar(f"graph TD\nJ1['Evaluate']\nJ1 --> J2['Refine']\nJ2 --> J3['Expand']\nJ3 --> J4([End])\n{styles}\nclass J1,J3 mainNode; class J2 subNode; class J4 startEnd;")

# --- DOWNLOAD INSTRUCTIONS ---
st.markdown("---")
with st.expander("📥 **How to Download / Save this Dashboard**"):
    st.markdown("""
    To save this entire dashboard as a professional **Landscape PDF or Image**:
    1. **Press** `Ctrl + P` (Windows) or `Cmd + P` (Mac).
    2. **Set Destination** to 'Save as PDF'.
    3. **Change Layout** to 'Landscape'.
    4. **Enable 'Background Graphics'** (under More Settings/Options) to ensure colors appear.
    5. **Click Save.**
    """)
