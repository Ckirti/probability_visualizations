import streamlit as st
import matplotlib.pyplot as plt
import random

def animate_coin_flips(num_flips, bias=0.5):
    """Creates a static bar chart."""
    results = [random.random() < bias for _ in range(num_flips)]
    heads_count = sum(results)
    tails_count = num_flips - heads_count

    plt.figure(figsize=(6, 6))
    plt.bar(['Heads', 'Tails'], [heads_count, tails_count], color=['skyblue', 'salmon'])
    plt.title(f'Coin Flip Simulation (Bias={bias})')
    plt.ylabel('Count')

    st.pyplot(plt) # display the static chart.

st.title("Animated Coin Flip Simulation")
num_flips = st.slider("Number of Flips", 10, 500, 100)
bias = st.slider("Bias (Probability of Heads)", 0.0, 1.0, 0.5)

animate_coin_flips(num_flips, bias) #remove session state, for testing.
