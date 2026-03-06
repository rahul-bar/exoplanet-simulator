import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("Exoplanet Orbit Simulator")

# Controls
radius = st.slider("Orbit Radius (AU)", 0.5, 5.0, 1.0)
period = st.slider("Orbital Period (days)", 1, 50, 10)
planet_size = st.slider("Planet Size", 5, 20, 10)

# Time array
t = np.linspace(0, 2*np.pi, 200)

x = radius*np.cos(t)
y = radius*np.sin(t)

frames = []

for i in range(len(t)):
    frames.append(
        go.Frame(
            data=[
                go.Scatter(
                    x=[x[i]],
                    y=[y[i]],
                    mode="markers",
                    marker=dict(size=planet_size)
                )
            ]
        )
    )

fig = go.Figure(
    data=[
        go.Scatter(x=[0], y=[0], mode="markers", marker=dict(size=40), name="Star"),
        go.Scatter(x=[x[0]], y=[y[0]], mode="markers", marker=dict(size=planet_size), name="Planet")
    ],
    layout=go.Layout(
        xaxis=dict(range=[-5,5]),
        yaxis=dict(range=[-5,5]),
        title="Planet Orbit Animation",
        updatemenus=[{
            "type": "buttons",
            "buttons":[{"label":"Play","method":"animate","args":[None]}]
        }]
    ),
    frames=frames
)

st.plotly_chart(fig)
