import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def animate_die_rolls(num_rolls):
    """Animates die rolls and displays the results."""
    results = []
    counts = [0] * 6

    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(range(1, 7), counts, color='lightgreen')
    ax.set_title('Die Roll Simulation')
    ax.set_xlabel('Die Face')
    ax.set_ylabel('Count')
    ax.set_xticks(range(1, 7))

    def update(frame):
        roll = random.randint(1, 6)
        results.append(roll)
        counts[roll - 1] += 1
        for bar, count in zip(bars, counts):
            bar.set_height(count)
        ax.set_title(f'Die Roll Simulation (Rolls: {len(results)})')
        return bars

    ani = animation.FuncAnimation(fig, update, frames=num_rolls, interval=50, repeat=False)
    st.pyplot(fig)

st.title("Animated Die Roll Simulation")
num_rolls = st.slider("Number of Rolls", 10, 1000, 200)

animate_die_rolls(num_rolls)
