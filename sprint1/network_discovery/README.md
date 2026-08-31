# Sprint 1: Passive Network Discovery & Live Inventory 

> **Status:** All core scripts, database schemas, and automation tools are fully written and prepared. Execution will start immediately once the physical Raspberry Pi 5 hardware arrives.

---

##  Repository Contents

| File Name | Purpose / What it does |
| :--- | :--- |
| **`discovery.py`** | The core Python script that automates network scanning using `arp-scan` (for fast discovery) and `nmap` (for OS fingerprinting), then syncs the results to the database. |
| **`setup.sh`** | An automated Bash script to quickly update system packages and install required network tools (`nmap` and `arp-scan`) on the edge device. |
| **`schema.sql`** | The SQL blueprint defining the structure of the lightweight `SQLite` database (`devices` table) to store IP, MAC, Vendor, and timestamps. |
| **`.gitignore`** | Configured to prevent local database files (`*.db`) and python cache from being tracked or uploaded to GitHub. |

---

##  Execution Plan (Upon Hardware Arrival)

1. **Clone & Setup:**
   Run the automated installation script on the Raspberry Pi OS:
   ```bash
   bash setup.sh
