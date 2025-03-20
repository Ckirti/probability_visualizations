import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def animate_coin_flips(num_flips, bias=0.5):
    """Animates coin flips and displays the results."""
    results = []
    heads_counts = []
    tails_counts = []

    fig, ax = plt.subplots(figsize=(6, 6))
    bars = ax.bar(['Heads', 'Tails'], [0, 0], color=['skyblue', 'salmon'])
    ax.set_title(f'Coin Flip Simulation (Bias={bias})')
    ax.set_ylabel('Count')

    def update(frame):
        results.append(random.random() < bias)
        heads_count = sum(results)
        tails_count = len(results) - heads_count
        heads_counts.append(heads_count)
        tails_counts.append(tails_count)
        bars[0].set_height(heads_count)
        bars[1].set_height(tails_count)
        ax.set_title(f'Coin Flip Simulation (Bias={bias}, Flips: {len(results)})')
        return bars

    ani = animation.FuncAnimation(fig, update, frames=num_flips, interval=50, repeat=False)
    st.pyplot(fig)

st.title("Animated Coin Flip Simulation")
num_flips = st.slider("Number of Flips", 10, 500, 100)
bias = st.slider("Bias (Probability of Heads)", 0.0, 1.0, 0.5)

animate_coin_flips(num_flips, bias)
