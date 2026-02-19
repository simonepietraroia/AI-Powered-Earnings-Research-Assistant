# 📊 AI-Powered Earnings Research Assistant (R)

An AI-driven research assistant built in **R** to **augment financial analysts** by automating earnings data ingestion, structured financial modeling, scenario forecasting, and draft report generation — while preserving human judgment and oversight.

This system does **not** provide investment advice or replace analysts.  
It automates the mechanical layer of earnings analysis to improve productivity, accuracy, and consistency.

---

## 🚀 Project Overview

Financial analysts often spend hours each quarter on repetitive work:

- Collecting historical financial data
- Updating models
- Extracting guidance from earnings releases
- Calculating growth and margins
- Producing charts
- Drafting structured summaries

This project automates those tasks and produces **reviewable, auditable outputs**.

---

## 🧠 Core Capabilities

### 📥 Hybrid Data Ingestion
- Automatically retrieves **5–7 historical quarters** of structured financial data (e.g., SEC XBRL for US-listed companies)
- Accepts latest earnings release as a **PDF upload**
- Extracts guidance and qualitative highlights

### 🔍 Evidence-Grounded Extraction
- Numeric fields extracted from PDFs include:
  - Evidence snippet
  - Page number
  - Deterministic validation
- **Zero hallucinated financial data** (numbers must be verifiable)

### 📈 Deterministic Financial Modeling
- CAGR-based forecasting (for limited history)
- Regression-based trend forecasting (when enough quarters exist)
- Scenario modeling (**Base / Bull / Bear**)
- Guidance-anchored projections (when guidance exists)
- Data sufficiency enforcement

### 📊 Visualization
- Revenue history + forecast charts
- Margin trend charts
- Scenario comparison charts

### 📝 Draft Report Generation
- Template-driven analyst-style draft summaries
- Neutral analytical tone
- No investment ratings or price targets
- Fully grounded in validated data

### 🧑‍💼 Human-in-the-Loop Design
- Analysts can override:
  - Growth assumptions
  - Margin assumptions
  - Forecast horizon
- Draft output is intended for analyst review before publication

---

## 🏗 System Architecture

```text
User Input (Ticker + Earnings PDF)
            ↓
Historical Data Retrieval
            ↓
PDF Parsing & LLM Extraction
            ↓
Deterministic Validation
            ↓
Structured Financial Store
            ↓
Forecast & Scenario Engine
            ↓
Chart Generation
            ↓
Draft Report Generation
            ↓
Analyst Review
