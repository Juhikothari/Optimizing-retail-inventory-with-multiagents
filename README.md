# 🛒 Optimizing Retail Inventory with Multi-Agents

This Streamlit-powered web app leverages data-driven techniques to optimize key retail operations:
- 📦 Inventory Redistribution
- 💰 Pricing Optimization
- 📊 Sales Forecasting (coming soon)

It provides a unified dashboard for retail managers to make smart, data-backed decisions using real-time inputs.

---

## 🚀 Features

### 📦 Inventory Monitoring & Redistribution
- Identifies **low-stock** and **high-stock** situations
- Recommends smart **inter-store transfers** based on threshold logic

### 💰 Pricing Optimization
- Uses **Linear Regression** to predict optimal pricing
- Displays **current vs optimized prices** with % change

### 📊 Sales Forecasting *(Planned)*
- Placeholder for future sales trend prediction models (e.g., Prophet)

---

## 🖥️ How to Run

### 🔧 Prerequisites
- Python 3.8+
- Install the required libraries:

```bash
pip install -r requirements.txt
```

### ▶️ Run the app

```bash
streamlit run retail_clean.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📁 File Structure

```
📦 your-repo/
├── retail_clean.py          # Streamlit app code
├── requirements.txt         # Required packages
├── data/                    # (Optional) Sample CSV files
└── screenshots/             # (Optional) UI images
```

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- NumPy

---

## 💡 Future Scope

- Integrate Facebook Prophet for sales forecasting
- Add charts & analytics
- Deploy to Streamlit Cloud or Hugging Face Spaces

---

## 📷 Screenshots

![Dashboard Overview](screenshots/dashboard.png)


---

## 👥 Author

- JUHI KOTHARI

---

## 📄 License

This project is open-source and free to use under the [MIT License](LICENSE).
