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
├── data_collection.ipynb
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
3. Prepare the Data
   Open the notebook:  
   `data_collection.ipynb`
   
   Follow the instructions to fetch and save the raw Gensyn testnet data (e.g. from Alchemy).
   
   Ensure the file `gensyn_transactions_flat_full.csv` is saved in the project root directory.

4.  Run the Analysis Pipeline

   Open and run:  
   `analysis_script.ipynb`
   
   This notebook processes the raw data and generates all output files into the `processed/` folder.
   
   > **Note:** Output `.csv` files are **not included** in the repository due to file size (~1 GB). You must generate them locally by running the notebook.

5. Run the Streamlit dashboard
   ```bash
   streamlit run dashboard.py
   ```
---
