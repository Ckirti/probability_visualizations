import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time

def animate_coin_flips_cumulative(num_flips, bias=0.5, placeholder=None):
    """Animates coin flips and displays cumulative heads count with persistence."""
    results = []
    heads_counts = []
    tails_counts = []

    fig, ax = plt.subplots(figsize=(6, 6))
    bars = ax.bar(['Heads', 'Tails'], [0, 0], color=['skyblue', 'salmon'])
    ax.set_title(f'Coin Flip Simulation (Bias={bias})')
    ax.set_ylabel('Count')
    ax.set_ylim(0, num_flips)

    def update(frame):
        results.append(random.random() < bias)
        heads_count = sum(results)
        tails_count = len(results) - heads_count
        heads_counts.append(heads_count)
        tails_counts.append(tails_counts)
        bars[0].set_height(heads_count)
        bars[1].set_height(tails_count)
        ax.set_title(f'Coin Flip Simulation (Bias={bias}, Flips: {len(results)})')
        return bars

    ani = animation.FuncAnimation(fig, update, frames=num_flips, interval=50, repeat=False)

    if placeholder:
        placeholder.pyplot(fig)

    # Display the final frame statically and persist
    if placeholder:
        for _ in range(num_flips):
          update(_)
        st.session_state.final_fig = fig #store the final figure.
        placeholder.pyplot(fig)
        #time.sleep(10)
        placeholder.empty()

    return ani

st.title("Cumulative Coin Flip Animation with Persistence")
num_flips = st.slider("Number of Flips", 100, 10000, 100)
bias = st.slider("Bias (Probability of Heads)", 0.0, 1.0, 0.5)

if 'cumulative_simulation' not in st.session_state:
    st.session_state.cumulative_simulation = False

if not st.session_state.cumulative_simulation:
    plot_placeholder = st.empty()
    st.session_state.animation = animate_coin_flips_cumulative(num_flips, bias, placeholder=plot_placeholder)
    st.session_state.cumulative_simulation = True

#Display the final figure if it exists.
if 'final_fig' in st.session_state:
  st.pyplot(st.session_state.final_fig)

if st.button("Restart Simulation"):
    st.session_state.cumulative_simulation = False
    st.session_state.pop("final_fig", None) #remove the figure.
    st.rerun()
