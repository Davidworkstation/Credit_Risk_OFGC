import numpy as np
from scipy.stats import norm
import pandas as pd
import random
import streamlit as st
import warnings
import plotly.graph_objects as go

st.set_page_config(layout="wide")
st.markdown(
    f"""
    <h1 style='text-align: center;'>Credit Risk: One Factor Gaussian Copula</h1>
    """,
    unsafe_allow_html=True
)

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

col1, colmid, col2 = st.columns([4,1,20])

def hazard_rates_generation(hazard_rate_option, start=0.01, stop=1.0, hazard_set_value = 0.2):
    if hazard_rate_option == 'Random':
        hazard_rate = [random.random() for _ in range(Trials)]
        return hazard_rate
    elif hazard_rate_option == 'Increasing':
        hazard_rate = np.linspace(start,stop,Trials)
        return hazard_rate
    elif hazard_rate_option == 'Set':
        hazard_rate = [hazard_set_value] * Trials
        return hazard_rate

with col1:
    st.subheader('Input Values')
    Trials = st.number_input('Number of Trials', min_value=0,max_value=1000000,step=1,value=10)
    p = st.number_input('Probability of Default (p)', min_value=0.0,max_value=1.0,step=0.01,value=0.5)
    M = st.number_input('Market Factor (M)', min_value=-3.0,max_value=3.0,step=0.01,value=0.0)
    Z_values = norm.ppf(np.random.rand(Trials))
    hazard_rate_option = st.selectbox('Hazard Rate Array Options', options=['Random','Increasing','Set'])
    
    if hazard_rate_option == 'Random':
        hazard_rate = hazard_rates_generation(hazard_rate_option)
        
    elif hazard_rate_option == 'Increasing':
        inc_start = st.number_input('Start Value', min_value=0.0001,max_value=0.99,step=0.01,value=0.0001)
        inc_stop = st.number_input('Stop Value', min_value=0.1,max_value=1.0,step=0.01,value=1.0)
        hazard_rate = hazard_rates_generation(hazard_rate_option, start=inc_start, stop=inc_stop)

    elif hazard_rate_option == 'Set':
        Set_value = st.number_input('Set Value', min_value=0.0,max_value=0.99,step=0.01,value=0.2)
        hazard_rate = hazard_rates_generation(hazard_rate_option, hazard_set_value=Set_value)

si = [1 - hr for hr in hazard_rate]

correlated_x = []
for Zi in Z_values:
    x_cal1 = (np.sqrt(p)) * M
    x_cal2 = (np.sqrt(1 - p)) * Zi
    x_cal = x_cal1 + x_cal2
    correlated_x.append(x_cal)

x_normalized_Pi = []
for x_c in correlated_x:
    x_norm = norm.cdf(x_c)
    x_normalized_Pi.append(x_norm)

survival_barrier_values = []
for Pi in x_normalized_Pi:
    Pi_cal = 1 - Pi
    survival_barrier_values.append(Pi_cal)

time_to_default = []
for s, si_value in zip(survival_barrier_values, si): #change to "for loop" for s with a constant hazard rate
    t = np.log(s) / np.log(si_value)
    time_to_default.append(t)

rounded_values = [round(time) for time in time_to_default]
trials_list = [i for i in range(1, Trials + 1)]

Name = []
for h in trials_list:
    names = (f"Name {h}")
    Name.append(names)

data = pd.DataFrame({ 
    "Names":Name,
    "Hazard Rates":hazard_rate,
    "Zi":Z_values,
    "Correlated xi":correlated_x,
    "x normalized (Pi)":x_normalized_Pi,
    "Survival Barriers (1 - Pi)":survival_barrier_values,
    "time to default (Years)": time_to_default,
    "time to default (whole years)":rounded_values
})

def graph(data, xlabel, titlew, bin = 30, strt = 0, stp = 30, ylabel = 'Frequency', color = 'blue'):
    fig = go.Figure()
    hist = go.Histogram(
        x=data,
        nbinsx=bin,  # Number of bins
        marker_color=color,  # Color of the bars
        opacity=0.75  # Opacity of the bars
    )

    fig.update_xaxes(range=[strt,stp])
    fig.update_xaxes(title_text=xlabel)
    fig.update_yaxes(title_text=ylabel)
    fig.add_trace(hist)
    fig.update_layout(width=300, height=300)
    fig.update_layout(
        title = titlew
    )
    st.plotly_chart(fig)

with col2:
    st.dataframe(data, use_container_width = False, height=300)
    inner_columns = st.columns(3)
    
    with inner_columns[0]:
        graph(rounded_values, xlabel='Time To Default (Years)', titlew='Time to Default Histogram', color='#A7C7E7', bin=100)
    
    with inner_columns[1]:
        graph(Z_values, xlabel='Generated Z Values', titlew='Idiosyncratic Stochastic Values Histogram', color='#FFD1DC', strt=-5, stp=5)

    with inner_columns[2]:
        graph(survival_barrier_values, xlabel='Survival Barriers', titlew='Survival Barriers Histogram', color='#FDFD96', strt=0, stp=1)


