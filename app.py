import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(layout="wide", page_title="Gensyn Transaction Dashboard")

# Title
st.title("📊 Gensyn Analysis Dashboard")

# Load Data
@st.cache_data
def load_data():
    base_path = "processed"
    data = {
        "top_from_count": pd.read_csv(os.path.join(base_path, "top_from_count.csv"), index_col=0),
        "top_from_volume": pd.read_csv(os.path.join(base_path, "top_from_volume.csv"), index_col=0, header=None, names=["address", "eth_volume"]),
        "top_to_count": pd.read_csv(os.path.join(base_path, "top_to_count.csv"), index_col=0),
        "avg_gas_per_block": pd.read_csv(os.path.join(base_path, "avg_gas_per_block.csv")),
        "avg_congestion": pd.read_csv(os.path.join(base_path, "avg_congestion_per_block.csv")),
        "gas_cost_data": pd.read_csv(os.path.join(base_path, "gas_cost_data.csv")),
        "top_contracts_by_tx": pd.read_csv(os.path.join(base_path, "top_contracts_by_tx.csv")),
        "top_contracts_by_gas": pd.read_csv(os.path.join(base_path, "top_contracts_by_gas.csv")),
        "contract_gas_efficiency": pd.read_csv(os.path.join(base_path, "contract_gas_efficiency.csv")),
        "top_spenders": pd.read_csv(os.path.join(base_path, "top_spenders.csv")),
        "top_value_to_gas_ratio": pd.read_csv(os.path.join(base_path, "top_value_to_gas_ratio.csv")),
        "zscore_anomalies": pd.read_csv(os.path.join(base_path, "zscore_anomalies.csv")),
        "kmeans_outliers": pd.read_csv(os.path.join(base_path, "kmeans_outliers.csv")),
        "input_size_anomalies": pd.read_csv(os.path.join(base_path, "input_size_anomalies.csv")),
        "congestion_ratio_all_tx": pd.read_csv(os.path.join(base_path, "congestion_ratio_all_tx.csv")),
        "block_congestion_unique": pd.read_csv(os.path.join(base_path, "block_congestion_unique.csv")),
    }
    return data

data = load_data()

# Sidebar
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", [
    "Top Addresses",
    "Gas Trends",
    "Smart Contract Interactions",
    "Anomalies",
    "Efficiency Analysis"
])

# Top Addresses Section
if section == "Top Addresses":
    st.subheader("🔝 Top Addresses by Activity")

    col1, col2 = st.columns(2)
    with col1:
        st.write("### From Addresses by Count")
        st.dataframe(data["top_from_count"])

    with col2:
        st.write("### From Addresses by ETH Volume")
        st.dataframe(data["top_from_volume"])

    st.write("### To Addresses by Count")
    st.dataframe(data["top_to_count"])

# Gas Trends Section
elif section == "Gas Trends":
    st.subheader("⛽ Gas Usage & Congestion Trends")

    st.write("### Average Gas per Block")
    st.line_chart(data["avg_gas_per_block"].set_index("block_number"))

    st.write("### Average Congestion per Block")
    st.line_chart(data["avg_congestion"].set_index("block_number"))

    st.write("### Gas Cost Distribution")
    fig, ax = plt.subplots()
    data["gas_cost_data"]["gas_cost_eth"].hist(bins=50, color='green', edgecolor='black', ax=ax)
    ax.set_title("Gas Cost Distribution (ETH)")
    ax.set_xlabel("Gas Cost (ETH)")
    ax.set_ylabel("Transactions")
    st.pyplot(fig)

    st.write("### Congestion Ratio Distribution - All Transactions")
    fig2, ax2 = plt.subplots()
    data["congestion_ratio_all_tx"]["congestion_ratio"].hist(bins=50, color='skyblue', edgecolor='black', ax=ax2)
    ax2.set_title("Block Congestion Ratio (All Transactions)")
    ax2.set_xlabel("Gas Used / Gas Limit")
    ax2.set_ylabel("Transaction Count")
    ax2.grid(True, linestyle='--', alpha=0.6)
    st.pyplot(fig2)

    st.write("### Congestion Ratio Distribution - Unique Blocks")
    fig3, ax3 = plt.subplots()
    data["block_congestion_unique"]["congestion_ratio"].hist(bins=50, color='orange', edgecolor='black', ax=ax3)
    ax3.set_title("Block Congestion Ratio (Unique Blocks)")
    ax3.set_xlabel("Gas Used / Gas Limit")
    ax3.set_ylabel("Block Count")
    ax3.grid(True, linestyle='--', alpha=0.6)
    st.pyplot(fig3)

# Smart Contract Interactions Section
elif section == "Smart Contract Interactions":
    st.subheader("📄 Smart Contract Interactions")

    col1, col2 = st.columns(2)
    with col1:
        st.write("### Top Contracts by Tx Count")
        st.dataframe(data["top_contracts_by_tx"])

    with col2:
        st.write("### Top Contracts by Total Gas")
        st.dataframe(data["top_contracts_by_gas"])

    st.write("### Gas Efficiency Metrics (Top Contracts)")
    st.dataframe(data["contract_gas_efficiency"])

# Efficiency Analysis Section
elif section == "Efficiency Analysis":
    st.subheader("⚙️ Gas vs Value Efficiency")

    st.write("### Top Wallets by Gas Spent (ETH)")
    st.dataframe(data["top_spenders"])

    st.write("### Top Value-to-Gas Ratio Transactions")
    st.dataframe(data["top_value_to_gas_ratio"])

# Anomaly Section
elif section == "Anomalies":
    st.subheader("🚨 Anomaly Detection")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Z-Score Anomaly Transactions", len(data["zscore_anomalies"]))
        st.dataframe(data["zscore_anomalies"].head())

    with col2:
        st.metric("Input Size Anomaly Transactions", len(data["input_size_anomalies"]))
        st.dataframe(data["input_size_anomalies"].head())

    st.write("### Clustering-Based Outliers")
    st.metric("KMeans Outliers", len(data["kmeans_outliers"]))
    st.dataframe(data["kmeans_outliers"].head())

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using [Streamlit](https://streamlit.io/)")
