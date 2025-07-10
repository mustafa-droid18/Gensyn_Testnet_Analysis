# 🚀 Gensyn Testnet Data Analysis

This project analyzes public transaction data from the Gensyn Testnet to uncover key activity patterns, smart contract interactions, network congestion, gas efficiency, and anomalous behavior.

### 📊 Features

- Top active addresses by transaction count and ETH volume
- Gas usage trends and congestion ratio distributions
- Smart contract interaction analysis and input size metrics
- Anomaly detection using z-scores and clustering (KMeans)
- Gas efficiency metrics (value vs gas spent)
- Streamlit dashboard for interactive visualization

### 📦 Project Structure
```
├── app.py # Streamlit dashboard app
├── analysis_script.ipynb 
├── processed/
│ ├── top_from_count.csv
│ ├── avg_gas_per_block.csv
│ └── ...
├── README.md
├── requirements.txt
└── Gensyn_Testnet_Data_Analysis.pdf
```

### 📈 Technologies Used

- Python (Pandas, NumPy, Matplotlib, Scikit-learn)
- Streamlit
- Jupyter (for exploration)
- Alchemy API (for Gensyn access)

### 🚀 How to Run

1. Clone the repo  
   ```bash
   git clone https://github.com/YOUR_USERNAME/gensyn-data-analysis.git
   cd Gensyn_Testnet_Analysis
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit dashboard
   ```bash
   streamlit run dashboard.py
   ```
---
