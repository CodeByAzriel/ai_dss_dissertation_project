# Designing a Digital Twin-Based AI Decision Support System for Cybersecurity Threat Prediction and Risk Mitigation

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Academic Standard](https://img.shields.io/badge/Academic-Honours%20Research-success.svg)]()

## 📋 Overview
This repository contains the core software artifact and empirical evaluation pipeline for an Honours research dissertation at Eduvos. The project proposes a novel **Digital Twin-Based Artificial Intelligence Decision Support System (AI-DSS)** designed to bridge the contextual blind spots inherent in standalone machine learning intrusion detection systems (IDS). 

By uniting predictive machine learning analytics (XGBoost), live virtual network topology simulation, and a structured decision-support mitigation layer, the system transitions enterprise security from reactive firefighting to proactive resilience.

---

## 🏗️ Project Architecture & File Structure

The codebase is engineered following modular software design principles:

```text
ai_dss_dissertation_project/
│
├── datasets/                   # Benchmark CIC-IDS2017 CSV files (Ignored via .gitignore)
├── preprocessing.py            # Automated data cleaning, feature extraction, and SMOTE balancing
├── train_model.py              # ML classifier training (Random Forest baseline & XGBoost ensemble)
├── compare_models.py           # Comparative performance evaluation and confusion matrix generation
├── digital_twin_sim.py         # Topological network sandbox and telemetry synchronization simulator
├── dss_engine.py               # Decision Support System translating anomaly scores into actionable directives
└── main_pipeline.py            # Primary orchestration script executing the end-to-end evaluation flow
