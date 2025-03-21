import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def animate_two_dice_sums(num_rolls):
    """Animates rolling two dice and displays the sum distribution."""
    sums = []
    counts = [0] * 11  # Sums range from 2 to 12

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(range(2, 13), counts, color='lightblue')
    ax.set_title('Two Dice Sum Simulation')
    ax.set_xlabel('Sum of Dice')
    ax.set_ylabel('Count')
    ax.set_xticks(range(2, 13))

    def update(frame):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        total_sum = roll1 + roll2
        sums.append(total_sum)
        counts[total_sum - 2] += 1
        for bar, count in zip(bars, counts):
            bar.set_height(count)
        ax.set_title(f'Two Dice Sum Simulation (Rolls: {len(sums)})')
        return bars

    ani = animation.FuncAnimation(fig, update, frames=num_rolls, interval=50, repeat=False)
    st.pyplot(fig)

st.title("Animated Two Dice Sum Simulation")
num_rolls = st.slider("Number of Rolls", 10, 5000, 1000)

animate_two_dice_sums(num_rolls)
