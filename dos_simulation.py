import streamlit as st
import requests
import time
import psutil

# Simulated target server (change to any valid test server)
TEST_SERVER = "http://httpbin.org/get"  # Public API for testing

def send_requests(num_requests):
    """Function to send multiple requests to a target server."""
    start_time = time.time()
    response_times = []

    for _ in range(num_requests):
        try:
            before = time.time()
            response = requests.get(TEST_SERVER)
            after = time.time()
            response_times.append(after - before)
        except requests.exceptions.RequestException:
            response_times.append(None)

    total_time = time.time() - start_time
    return response_times, total_time

def simulate_attack(num_requests):
    """Simulates a DoS attack by sending multiple requests."""
    cpu_usage_before = psutil.cpu_percent()
    response_times, attack_duration = send_requests(num_requests)
    cpu_usage_after = psutil.cpu_percent()
    
    return response_times, attack_duration, cpu_usage_before, cpu_usage_after

# Streamlit UI
st.title("Denial of Service (DoS) Attack Simulation")
st.markdown("<h2 style='color: blue;'>This app simulates a simple DoS attack</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='color: green;'>Flooding a test server with multiple requests.</h3>", unsafe_allow_html=True)

num_requests = st.slider("Number of Requests", min_value=10, max_value=1000, step=10, value=100)

if st.button("Simulate Attack"):
    st.write("Simulating attack... Please wait.")

    response_times, attack_duration, cpu_before, cpu_after = simulate_attack(num_requests)

    st.success(f"Attack completed in {attack_duration:.2f} seconds.")
    st.write(f"CPU Usage Before Attack: {cpu_before}%")
    st.write(f"CPU Usage After Attack: {cpu_after}%")

    if response_times:
        st.line_chart(response_times)
        st.write("Above chart shows response time for each request (spikes indicate delays).")

st.write("Disclaimer: This is a simulated attack. Do not perform this on unauthorized systems.")
