import streamlit as st
import graphviz

# Set page config
st.set_page_config(page_title="MTI Pathway Visualizer", layout="wide")

st.title("MTI Pathway – Trust-Level Visual Flow")
st.subheader("Infection Sciences Model")

# Define the flowchart logic
def generate_flowchart():
    dot = graphviz.Digraph(comment='MTI Pathway')
    dot.attr(rankdir='TB', size='10')
    dot.attr('node', shape='rectangle', style='filled', color='lightblue', fontname='Arial')

    # 1. Strategic Intent
    dot.node('1', '1. Strategic Intent & Service Need\n- Identify Gap\n- Align with Strategy\n- Agreement in Principle')

    # 2. Programme Design
    dot.node('2', '2. Programme Design\n- Define Post (12-24m)\n- Confirm Training Value\n- Identify Supervisors')

    # 3. Governance
    dot.node('3', '3. Governance & Approvals\n- Engage Stakeholders\n- Royal College Sponsorship\n- Trust Approval')

    # 4. Pipeline
    dot.node('4', '4. International Candidate Pipeline\n- Identify Partner\n- Candidate EOI\n- Shortlisting & Interview')

    # 5. Pre-Arrival
    dot.node('5', '5. Pre-Arrival Preparation\n- GMC Registration\n- Visa Sponsorship (Tier 5)\n- Pre-arrival Engagement')

    # 6. Induction
    dot.node('6', '6. Induction & Safe Transition\n- Trust & Dept Induction\n- Supernumerary Period\n- Clinical Integration')

    # 7. Training
    dot.node('7', '7. Training Delivery & Support\n- Structured Programme\n- Regular Supervision\n- Teaching & QI')

    # 8. Monitoring
    dot.node('8', '8. Monitoring & Quality Assurance\n- 3/6/12 Month Reviews\n- Feedback Collection\n- Address Issues Early')

    # 9. Completion
    dot.node('9', '9. Programme Completion & Exit\n- Final Review & Sign-off\n- Return to Home Country\n- Capture Outcomes')

    # 10. Improvement
    dot.node('10', '10. Continuous Improvement Loop\n- Evaluate & Refine\n- Expand Capacity')

    # Define Connections
    edges = [('1', '2'), ('2', '3'), ('3', '4'), ('4', '5'), ('5', '6'), 
             ('6', '7'), ('7', '8'), ('8', '9'), ('9', '10'), ('10', '1')]
    dot.edges(edges)

    return dot

# Display the chart
st.graphviz_chart(generate_flowchart())

st.info("This flowchart represents the end-to-end lifecycle of the MTI pathway within the Trust.")
