
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="AI Compression Visualizer", layout="centered")
st.title("AI Compression Metrics")

# Simulated API response
api_data = {
    "fidelity": 0.993,
    "speed": "1M tokens/sec",
    "compression": 11.3
}

st.metric("Fidelity", f"{api_data['fidelity']*100:.2f}%")
st.metric("Speed", api_data['speed'])

# Compression Bar
fig = go.Figure(go.Bar(
    x=["Original", "Compressed"],
    y=[100, 100 / api_data['compression']],
    marker_color=["gray", "green"]
))
fig.update_layout(title="Compression Comparison", yaxis_title="Size", xaxis_title="Version")
st.plotly_chart(fig)
