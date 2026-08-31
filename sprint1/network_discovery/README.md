# Sprint 1: Network Discovery & Hybrid Architecture 

> **Status:** All core scripts, database schemas, and automation tools are fully written and prepared. Execution will start immediately once the physical Raspberry Pi 5 hardware arrives.

---

## Overview & Architectural Rationale (Why Hybrid?)
The primary goal of this sprint is to build an instant and accurate device inventory. However, **pure passive listening is insufficient at startup** because idle or sleeping IoT devices (like smart sensors and printers) send no traffic for hours, leaving the dashboard empty. 

To solve this, "Assas" relies on an engineered **Two-Phase Hybrid Architecture**:
1. **Phase 1 - Initial Active Discovery (Boot-up):** A fast, lightweight active sweep using `arp-scan` and `nmap` instantly forces all connected devices to respond, building an immediate baseline inventory and overcoming the sleeping IoT problem.
2. **Phase 2 - Continuous Passive Monitoring:** Once the initial inventory is established, active scanning stops completely. The system shifts 100% to silent, passive monitoring to track behavior without disrupting the network.

---

##  Repository Contents

| File Name | Purpose / What it does |
| :--- | :--- |
| **`discovery.py`** | The core Python script executing our hybrid logic. It uses `arp-scan` for fast subnet mapping and integrates **built-in MAC vendor lookup and OS fingerprinting** to accurately detect device types. |
| **`setup.sh`** | An automated Bash script to quickly update system packages and install required network tools (`nmap` and `arp-scan`) on the edge device. |
| **`schema.sql`** | The SQL blueprint defining the structure of the lightweight `SQLite` database (`devices` table) to store IP, MAC, Vendor, and timestamps. |
| **`.gitignore`** | Configured to prevent local database files (`*.db`) and python cache from being tracked or uploaded to GitHub. |

---

##  Execution Plan (Upon Hardware Arrival)

1. **Clone the Repository:**
   Download the project files onto your Raspberry Pi edge device.

2. **Run the Setup Script:**
   Execute the automated installation script to update system packages and install networking tools:
   ```bash
   bash setup.sh
