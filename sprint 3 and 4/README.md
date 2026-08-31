# Sprints 3 & 4: Anomaly Detection, Behavioral Baselining & Explainable AI (XAI)

This directory contains the initial prototype and development verification artifacts for **Sprint 3 (Intelligence & Anomaly Detection)** and **Sprint 4 (Scoring & Explainability)**.

---

## 1. Technical Scope Breakdown

### **Sprint 3: Behavioral Baselining & ML Anomaly Detection**
* **Objective:** Establish baseline traffic behavior profiles per connected device and train an unsupervised/semi-supervised ML model to isolate anomalous network flows.
* **Core Tasks:**
  * Define and validate a unified 5-tuple statistical flow feature vector schema.
  * Train an `Isolation Forest` ensemble model exclusively on benign baseline distributions.
  * Evaluate decision boundaries and isolate anomalous/injected attack vectors.

### **Sprint 4: Risk Scoring Engine & Explainable AI (XAI)**
* **Objective:** Translate raw machine learning decision scores into an intuitive 0–100 risk scale and compute mathematical feature attributions explaining each alert.
* **Core Tasks:**
  * Implement the `Dynamic Risk Score Engine (0–100)` to normalize complex decision boundaries for non-technical home users.
  * Integrate `SHAP (TreeExplainer)` to calculate exact Shapley contribution weights for anomalous flow features.
  * Format feature explanations into structured JSON payloads for downstream alerting and LLM chatbot translation.

---

## 2. Tools & Workload Classification

| Component | Type | Description / Responsibility |
| :--- | :--- | :--- |
| **`scikit-learn`** | Ready-to-Use Library | Foundational implementation of the `IsolationForest` ensemble algorithm. |
| **`SHAP`** | Ready-to-Use Library | Game-theoretic algorithmic framework for computing Shapley feature contributions. |
| **`pandas` / `NumPy`** | Ready-to-Use Libraries | Matrix manipulation and structured DataFrame operations. |
| **`nfstream`** | Ready-to-Use Library | Bidirectional network flow feature extraction engine. |
| **CIC-IoT2023 & IoT-23** | Public Datasets | Real-world benchmark IoT datasets for offline model baseline training and validation. |
| **Device Baselining Engine** | Custom Development | Custom algorithmic pipeline constructing per-device (MAC/IP) statistical profiles instead of static global thresholds. |
| **Risk Scoring Engine** | Custom Development | Proprietary mathematical formula mapping raw model decision boundaries to a 0–100 dynamic risk score. |
| **XAI Alert Packaging** | Custom Development | Backend data structuring layer extracting top-$N$ SHAP features and packaging them into clean alert payloads. |

---

## 3. Directory Structure

```text
sprint_3_and_4/
├── code/
│   └── sprint3_4_anomaly_detection_and_xai.ipynb   # Verified Jupyter Notebook running detection, scoring & SHAP
├── data_samples/
│   └── iot23_sample.log                            # Lightweight sample extracted from IoT-23 benchmark
└── README.md                                       # Sprint documentation & scope breakdown
