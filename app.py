import streamlit as st
import graphviz

st.set_page_config(page_title="MTI Pathway Visualizer", layout="wide")

st.title("MTI Pathway – Trust-Level Visual Flow")
st.write("Visualizing the Infection Sciences Model")

def generate_swimlane_chart():
    # Use 'dot' engine for hierarchical layouts
    dot = graphviz.Digraph(comment='MTI Pathway', engine='dot')
    dot.attr(rankdir='LR', size='12,12') # Left to Right flow between lanes
    dot.attr('node', shape='rectangle', style='filled', fontname='Arial', fontsize='10')

    # --- LANE 1: Strategic & Programme Design ---
    with dot.subgraph(name='cluster_0') as c:
        c.attr(label='1. Strategic & Programme Design', bgcolor='#f0f0f0', style='filled', color='#2c3e50')
        c.node('S1', 'Start', shape='oval', fillcolor='#d4edda')
        c.node('S2', 'Strategic Intent', fillcolor='#34495e', fontcolor='white')
        c.node('S3', 'Programme Design\n(Role, Objectives, Duration)', fillcolor='#34495e', fontcolor='white')
        c.node('S4', 'Clinical Director Approval', fillcolor='#bdc3c7')
        c.edge('S1', 'S2')
        c.edge('S2', 'S3')
        c.edge('S3', 'S4')

    # --- LANE 2: Governance & Candidate Sourcing ---
    with dot.subgraph(name='cluster_1') as c:
        c.attr(label='2. Governance & Candidate Sourcing', bgcolor='#ffffff', style='filled', color='#2c3e50')
        c.node('G1', 'Stakeholder Engagement\n(Med Ed, HR, Finance)', fillcolor='#34495e', fontcolor='white')
        c.node('G2', 'Trust Approval', shape='parallelogram', fillcolor='#bdc3c7')
        c.node('G3', 'Identify International Partner\n& Royal College Sponsor', fillcolor='#34495e', fontcolor='white')
        c.edge('G1', 'G2')
        c.edge('G2', 'G3')

    # --- LANE 3: Pre-Arrival & Induction ---
    with dot.subgraph(name='cluster_2') as c:
        c.attr(label='3. Pre-Arrival & Induction', bgcolor='#f0f0f0', style='filled', color='#2c3e50')
        c.node('P1', 'GMC Registration', fillcolor='#bdc3c7')
        c.node('P2', 'Visa Sponsorship\n(Tier 5)', fillcolor='#bdc3c7')
        c.node('P3', 'Pre-arrival Engagement\n(Induction Plan)', fillcolor='#bdc3c7')
        c.edge('P1', 'P2')
        c.edge('P2', 'P3')

    # --- LANE 4: Training & Monitoring ---
    with dot.subgraph(name='cluster_3') as c:
        c.attr(label='4. Training & Monitoring', bgcolor='#ffffff', style='filled', color='#2c3e50')
        c.node('T1', 'Structured Training\n(Lab & MDT)', fillcolor='#34495e', fontcolor='white')
        c.node('T2', 'Regular Supervision\n(ES/CS Meetings)', fillcolor='#bdc3c7')
        c.node('T3', 'Feedback & Reviews', shape='diamond', fillcolor='#3498db', fontcolor='white')
        c.edge('T1', 'T2')
        c.edge('T2', 'T3')

    # --- LANE 5: Programme Exit & Improvement ---
    with dot.subgraph(name='cluster_4') as c:
        c.attr(label='5. Programme Exit & Improvement', bgcolor='#f0f0f0', style='filled', color='#2c3e50')
        c.node('E1', 'Final Sign-off', fillcolor='#34495e', fontcolor='white')
        c.node('E2', 'Capture Outcomes', fillcolor='#bdc3c7')
        c.node('E3', 'End', shape='oval', fillcolor='#d4edda')
        c.edge('E1', 'E2')
        c.edge('E2', 'E3')

    # Connect the Lanes
    dot.edge('S4', 'G1')
    dot.edge('G3', 'P1')
    dot.edge('P3', 'T1')
    dot.edge('T3', 'E1')
