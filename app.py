import streamlit as st
import sys
import subprocess

# Safety Check: Let's see if graphviz is actually installed
try:
    import graphviz
except ImportError:
    st.error("Python module 'graphviz' not found. Please ensure it is in requirements.txt")
    st.stop()

st.set_page_config(page_title="MTI Pathway Visualizer", layout="wide")

st.title("MTI Pathway – Trust-Level Visual Flow")

def generate_flowchart():
    # We use 'dot' engine explicitly
    dot = graphviz.Digraph(comment='MTI Pathway', engine='dot')
    dot.attr(rankdir='TB', size='10')
    dot.attr('node', shape='rectangle', style='filled', color='#E1F5FE', fontname='Arial', penwidth='2')
    
    # Process Steps
    steps = [
        ('1', '1. Strategic Intent & Service Need'),
        ('2', '2. Programme Design'),
        ('3', '3. Governance & Approvals'),
        ('4', '4. International Candidate Pipeline'),
        ('5', '5. Pre-Arrival Preparation'),
        ('6', '6. Induction & Safe Transition'),
        ('7', '7. Training Delivery & Support'),
        ('8', '8. Monitoring & Quality Assurance'),
        ('9', '9. Programme Completion & Exit'),
        ('10', '10. Continuous Improvement Loop')
    ]

    for id, label in steps:
        dot.node(id, label)

    # Simple sequential flow
    for i in range(1, 10):
        dot.edge(str(i), str(i+1))
        
    return dot

try:
    st.graphviz_chart(generate_flowchart())
except Exception as e:
    st.error(f"The Graphviz binary is missing or not linked. Error: {e}")
    st.info("Since you have packages.txt, try deleting the app on Streamlit Cloud and redeploying from scratch to clear the cache.")
