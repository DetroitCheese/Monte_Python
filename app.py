import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run_simulation(trials):
    tosses = np.random.choice(['Heads', 'Tails'], size=trials)
    heads_count = np.sum(tosses == 'Heads')
    tails_count = np.sum(tosses == 'Tails')
    return tosses, heads_count, tails_count

def plot_results(tosses):
    fig, ax = plt.subplots()
    ax.hist(tosses, bins=2)
    return fig

def plot_subset(subset):
    fig2, ax2 = plt.subplots()
    ax2.plot(subset, marker='o', linestyle='')
    return fig2

# Streamlit app
st.title('Monte Carlo Simulation of Coin Tosses')

trials = st.number_input('Enter the number of trials', min_value=1, max_value=1000000, value=1000)
tosses, heads_count, tails_count = run_simulation(trials)

st.write(f'Heads: {heads_count}')
st.write(f'Tails: {tails_count}')
st.pyplot(plot_results(tosses))

subset_size = st.number_input('Enter the number of flips to extract', min_value=1, max_value=trials, value=100)
subset = tosses[:subset_size]

st.write(f'Subset of {subset_size} flips: {subset}')
st.pyplot(plot_subset(subset))
