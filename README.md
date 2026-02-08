# Brent-Oil-Change-Point-Analysis
🛢️ Task 1: Laying the Foundation for Analysis

Change Point Analysis and Statistical Modeling of Brent Oil Prices

📌 Project Overview

This project is conducted for Birhan Energies, a consultancy firm providing data-driven insights to stakeholders in the energy sector.
The goal of Task 1 is to establish a strong analytical foundation for understanding how major geopolitical, economic, and policy events influence Brent oil prices over time.

Oil prices are highly volatile and sensitive to global events. By carefully examining historical price data and aligning it with key events, this task prepares the ground for Bayesian Change Point Analysis, which will be implemented in later stages of the project.

🎯 Objectives of Task 1

The main objectives of Task 1 are to:

Define a clear data analysis workflow

Understand the statistical properties of the Brent oil price time series

Compile a structured dataset of major global events

Clearly document assumptions and limitations

Identify appropriate communication channels for stakeholders

Prepare the analytical groundwork for Bayesian change point modeling

📊 Dataset Description
Brent Oil Price Data

Source: Historical Brent oil prices

Time Range: May 20, 1987 – September 30, 2022

Frequency: Daily

Fields:

Date: Date of observation (day-month-year)

Price: Brent oil price in USD per barrel

Event Data

A manually curated dataset of major events that may influence oil prices, including:

Geopolitical conflicts

OPEC policy decisions

Economic and global shocks

The event dataset contains:

date: Approximate start or announcement date

event: Short description

category: Type of event (e.g., OPEC Policy, Economic Shock)

🧭 Data Analysis Workflow

The analysis follows these steps:

Data Loading and Cleaning

Convert date fields to datetime format

Sort observations chronologically

Check for missing values

Exploratory Data Analysis (EDA)

Visualize raw Brent oil prices to identify trends and shocks

Compute log returns to stabilize variance

Observe volatility clustering

Time Series Diagnostics

Conduct stationarity testing using the Augmented Dickey-Fuller (ADF) test

Examine rolling mean and rolling standard deviation

Use findings to motivate probabilistic modeling

Event Data Integration

Align global events with price movements

Use event timing for interpretation only

Preparation for Change Point Modeling

Identify periods where structural breaks are likely

Avoid causal claims at this stage

📐 Assumptions

The analysis is based on the following assumptions:

Brent oil prices reflect public information available to market participants

Large structural breaks correspond to meaningful changes in market regimes

Log returns are approximately stationary and suitable for statistical modeling

Event dates represent approximate timing; markets may react before or after events

⚠️ Limitations and Causality Disclaimer
Correlation vs. Causation (Critical Distinction)

Statistical correlation in time means a price change occurs around the same time as an event

Causal impact requires proof that the event directly caused the price change

This analysis:

✅ Identifies temporal alignment

❌ Does not prove causality

Proving causation would require:

Control variables (e.g., GDP, inflation, exchange rates)

Counterfactual or causal inference methods

Natural experiments or instrumental variables

Additional limitations include:

Omission of macroeconomic and financial variables

Overlapping and interacting global events

Sensitivity to modeling assumptions

📢 Communication Channels

Results from this project are designed to be communicated through multiple channels:

Audience	Channel	Format
Policymakers	Policy brief	PDF with executive summary
Investors & Analysts	Dashboard	Interactive web application
Energy Companies	Technical report	Detailed PDF
Technical Reviewers	Jupyter Notebook	Reproducible analysis
General Stakeholders	Presentation	Slide deck with visuals

All communications emphasize uncertainty and probabilistic interpretation.

📁 Project Structure (Relevant to Task 1)
brent-oil-change-point-analysis/
├── data/
│   ├── raw/
│   │   └── brent_prices.csv
│   └── processed/
│       └── events.csv
├── notebooks/
│   └── 01_task1_eda_and_model_foundation.ipynb
├── reports/
│   └── task1_foundation.pdf
├── requirements.txt
└── README.md

📓 Notebook Description

01_task1_eda_and_model_foundation.ipynb includes:

Data loading and cleaning

Time series visualization

Log return computation

Stationarity testing (ADF)

Rolling statistics

Event alignment visualization

This notebook demonstrates readiness for Bayesian change point modeling without making causal claims.

✅ Deliverables Summary

✔️ Defined data analysis workflow

✔️ Structured event dataset (CSV)

✔️ Documented assumptions and limitations

✔️ Clear communication strategy

✔️ Reproducible Jupyter notebook