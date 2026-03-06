import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Exoplanet Transit Simulator")

# sliders
planet_radius = st.slider("Planet Radius (Earth radii)", 0.5, 5.0, 1.0)
orbit_period = st.slider("Orbital Period (days)", 1, 50, 10)
inclination = st.slider("Inclination (degrees)", 80, 90, 90)

# time array
t = np.linspace(-1, 1, 200)

# simple transit model
depth = (planet_radius/10)**2
light = 1 - depth*np.exp(-t**2*5)

# plot
fig, ax = plt.subplots()
ax.plot(t, light)
ax.set_xlabel("Time")
ax.set_ylabel("Relative Brightness")
ax.set_title("Transit Light Curve")

st.pyplot(fig)