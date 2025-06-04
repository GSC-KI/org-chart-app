import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# App title
st.title("Live Org Chart Editor")

# Sidebar inputs
top_label = st.selectbox("Top Label (Team Lead)", ["PDS", "MGG"])
project_label = st.text_input("Project Name", value="Project 1")
director_label = st.selectbox("Project Director", ["JBO", "ARV"])
engineer_label = st.selectbox("Engineer", ["GSC", "EMM"])

# Create the graph
G = nx.DiGraph()
edges = [
    (top_label, project_label),
    (project_label, director_label),
    (director_label, engineer_label)
]
G.add_edges_from(edges)

# Node positions
pos = {
    top_label: (0, 3),
    project_label: (0, 2),
    director_label: (0, 1),
    engineer_label: (0, 0)
}

# Draw chart
fig, ax = plt.subplots(figsize=(5, 6))
nx.draw(
    G, pos, ax=ax,
    with_labels=True,
    node_size=1,
    arrows=False,
    font_size=12,
    font_color='red',
    font_weight='bold',
    edge_color='red',
    width=2
)
ax.axis('off')
st.pyplot(fig)
