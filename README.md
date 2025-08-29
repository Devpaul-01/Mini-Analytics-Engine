

🛠️ Mini Analytics Engine

A Python-powered mini analytics engine that transforms nested retail data (regions → stores → customers → orders → items) into meaningful insights. It helps uncover customer behavior, store performance, and regional trends with ease.



🚀 Features

Region Analytics

Identify top-performing stores by revenue

Calculate average customer loyalty points per region


Store Analytics

Find the top customer by total spend

Detect the most popular product category

Measure average revenue per customer and per item


Customer Analytics

Track total spend and average order value

Highlight favorite product categories

Flag at-risk customers inactive for 60+ days


Flattened Data Export

Convert nested datasets into flat structures

Ready for CSV export, Pandas analysis, or database insertion





📂 Project Structure

mini-analytics-engine/
│
├── analytics.py — Core analytics functions
├── sample_data.py — Demo dataset (regions, stores, customers, etc.)
├── main.py — Run analytics and view outputs
└── README.md — Project documentation



📊 Example Insights

North Region → Store A is top performer with highest revenue

Store B → “Tie Customer” is top spender; popular categories include Home and Stationery

Customer “Old Timer” → flagged as at-risk due to long inactivity



🔮 Roadmap

Refactor into modular helper functions

Integrate Pandas for deeper analysis

Add visualizations with Matplotlib

Build an interactive dashboard (Streamlit / Dash / Flask + React)

Explore predictive analytics such as churn forecasting and sales trends



📦 Requirements

Python 3.8+

Standard library only (no external dependencies required yet)


🤝 Contributing

Contributions are welcome.
Open an issue to suggest improvements or submit a pull request with new features such as advanced KPIs, ML models, or visualizations.

