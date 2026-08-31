# Sprints 3 & 4: Technical Scope, Data Ingestion & Custom Implementation Breakdown

This document clarifies the prototype implementation scope for **Sprint 3 (Intelligence & Anomaly Detection)** and **Sprint 4 (Scoring & Explainability)**, outlining the separation between foundational tools and custom algorithm logic developed for the project.

---

## 1. Dataset Status & Ingestion Notice

* **CIC-IoT2023 Dataset (`CIC_IOT_Dataset2023/`):**
  * A lightweight, structured sample (`example.ipynb`) is committed directly to this repository to demonstrate successful ingestion, schema parsing, and feature extraction.
* **IoT-23 Dataset:**
  * The full dataset (8.7+ GB) has been successfully acquired, verified, and stored locally in our development environment. 
  * Due to GitHub repository storage limitations, the raw multi-gigabyte files are kept locally offline and will be loaded dynamically into the preprocessing scripts during local model baseline tuning.

---

## 2. Standard / Off-the-Shelf Tools & Libraries (Ready-to-Use)

* **`scikit-learn`:** Provides the underlying ensemble architecture (`IsolationForest`) for tree-based anomaly isolation.
* **`SHAP` (`TreeExplainer`):** Algorithmic framework used to calculate game-theoretic Shapley feature attributions.
* **`pandas` & `NumPy`:** Core libraries for structured 2D matrix transformations and array manipulation.
* **`nfstream` / `CICFlowMeter`:** Bidirectional network flow feature extraction engines.
* **CIC-IoT2023 & IoT-23:** Labeled public IoT benchmark datasets used as references for normal baseline behaviors and modern network attack vectors.

---

## 3. Custom Modules Developed from Scratch (Team Workload)

* **Per-Device Behavioral Baselining:** Custom mathematical modeling to profile each connected endpoint individually (MAC/IP baselines) using normal IoT traffic distributions, avoiding static, one-size-fits-all detection thresholds.
* **Feature Alignment & Preprocessing:** Custom ETL pipelines normalizing raw network captures into structured 5-tuple statistical flow vectors.
* **Dynamic Risk Scoring Engine (0–100):** A proprietary mathematical mapping function translating raw `decision_function()` distances into a human-interpretable risk metric for non-technical users.
* **Automated XAI Interpretation Pipeline:** Custom backend logic extracting the top-$N$ contributing SHAP feature attributions and structuring them into clean JSON payloads for downstream alerting.

---

## 4. Current Directory Structure

```text
gp/
└── sprint 3 and 4/
    ├── CIC_IOT_Dataset2023/
    │   └── example.ipynb                              # CIC-IoT sample ingestion & feature check
    ├── code/
    │   └── sprint3and4_anomaly_detection_shap...ipynb # Verified end-to-end ML & XAI pipeline
    └── ready_tools_vs_custom_work                     # Scope documentation & implementation note
