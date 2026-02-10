# Brent-Oil-Change-Point-Analysis
📊 Brent Oil Price Analysis

Change Point Detection & Interactive Dashboard

📌 Project Overview

This project analyzes historical Brent crude oil prices to understand how major geopolitical, economic, and policy events align with structural changes in oil price behavior.

The work is organized into three progressive tasks:

Task 1 – Exploratory Data Analysis (EDA) and statistical foundations

Task 2 – Bayesian Change Point Modeling and insight generation

Task 3 – Interactive dashboard for communicating results

The goal is insight, not prediction, with all findings communicated alongside uncertainty and limitations.

🧭 Project Structure
project-root/
│
├── data/
│   ├── raw/                # Raw Brent price data
│   ├── processed/          # Cleaned & transformed data
│   └── events/             # Structured geopolitical & economic events
│
├── notebooks/
│   ├── 01_eda.ipynb        # Task 1: EDA and diagnostics
│   └── 02_change_point.ipynb
│
├── src/
│   ├── data/
│   │   └── load_data.py
│   ├── eda/
│   │   └── eda.py
│   ├── models/
│   │   └── change_point.py
│   └── utils/
│       └── validation.py
│
├── dashboard/
│   ├── backend/            # Flask API (Task 3)
│   └── frontend/           # React app (Task 3)
│
├── data/results/
│   └── change_points.json
│
└── README.md

🧪 Task 1: Laying the Foundation (EDA & Diagnostics)
🎯 Objective

Establish a statistically sound understanding of Brent oil price behavior and prepare the data for change point modeling.

🔹 Step 1: Data Loading & Preparation

Load historical Brent oil prices

Convert Date to datetime format

Sort chronologically to preserve time order

Perform basic validation:

Missing values

Data type consistency

No interpolation or forward filling is applied to avoid artificial patterns

🔹 Step 2: Exploratory Data Analysis (EDA)

Plot raw price series to observe:

Long-term trends

Sharp spikes and collapses

Crisis periods

Compute log returns:

log(price_t) − log(price_{t−1})


This stabilizes variance and improves suitability for statistical modeling.

Visualize log returns to identify volatility clustering

🔹 Step 3: Time Series Diagnostics

Apply Augmented Dickey-Fuller (ADF) test

Raw prices: non-stationary

Log returns: stationary

Plot rolling mean and rolling standard deviation

Reveals changing statistical behavior over time

Motivates regime-based modeling

🔹 Step 4: Event Dataset Compilation

A structured CSV of major oil-relevant events is created, including:

Geopolitical conflicts

OPEC policy decisions

Economic and global health shocks

These events are aligned visually with the price series for interpretive analysis (not causal claims).

📌 Key Takeaways (Task 1)

Brent prices are non-stationary

Log returns are stationary and volatile

Evidence strongly suggests structural regime shifts

Data is well-prepared for Bayesian change point modeling

🔍 Task 2: Bayesian Change Point Modeling
🎯 Objective

Detect and quantify structural breaks in Brent oil prices using Bayesian inference.

🔹 Model Overview (Plain Explanation)

A Bayesian change point model assumes:

The data behaves differently before and after a certain unknown point in time

That change point is treated as a random variable, not a fixed date

The model estimates:

The most likely date of change

Average behavior before and after the change

Uncertainty around all estimates

🔹 Model Components

Switch point (τ)
Discrete uniform prior across all time indices

Before / After parameters (μ₁, μ₂)
Separate means for each regime

Likelihood
Normal distribution with mean selected using a switch function

Inference
MCMC sampling using PyMC

🔹 Model Evaluation

Convergence checked via:

r_hat ≈ 1.0

Trace plots

Posterior distribution of τ examined:

Sharp peak → high certainty

Parameter posteriors used to:

Quantify average price changes

Make probabilistic statements

🔹 Event Association

Detected change points are compared with known events to form hypotheses, such as:

“Following the OPEC production cut in 2016, the model detects a structural shift, with the average price increasing from X to Y.”

No causal claims are made.

📌 Outputs (Task 2)

Posterior distributions

Detected change points

Quantified impacts with uncertainty

Saved results in change_points.json

📊 Task 3: Interactive Dashboard Development
🎯 Objective

Translate analytical results into accessible, interactive insights for stakeholders.

🔧 Backend (Flask)

Provides APIs for:

Historical price data

Change point results

Event metadata

Example endpoints:

/api/prices

/api/change-points

/api/events

🎨 Frontend (React)

Interactive features include:

Time series visualization

Event highlighting

Date range filters

Drill-down exploration

Responsive design (desktop & mobile)

Recommended libraries:

Recharts

React Chart.js

D3.js (optional)

📌 Dashboard Insights

Visual alignment of price shifts and events

Volatility indicators

Regime comparison

Intuitive storytelling for non-technical users

⚠️ Limitations

Change point detection is probabilistic

Event alignment is interpretive, not causal

Model focuses on price behavior only (no external regressors yet)

🚀 Future Work

Incorporate macroeconomic variables (GDP, inflation, FX)

Explore:

Markov-switching models

VAR models

Extend dashboard with forecasting views