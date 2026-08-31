# Sprint 1: Passive Network Discovery & Live Inventory 

##  Overview (What & Why?)
Since our physical Raspberry Pi edge hardware is still on the way, we have prepared and structured all the foundational code, database schemas, and automation scripts for **Sprint 1**. 

The goal of this sprint is to achieve **Passive Network Discovery**. This allows our edge appliance ("Asas") to automatically scan the local network, identify connected devices (smartphones, laptops, IoT sensors), and track them without requiring any software installation on the user's devices.

---

## Files & Implementation Guide

Here is what each file in this repository does and how we plan to execute it once the hardware arrives:

### 1. `discovery.py` (The Core Script)
* **What it is:** The main Python script that acts as the brain for network discovery.
* **Why we built it:** It combines fast network scanning tools to find active devices efficiently.
* **How it works (Implementation Plan):**
  * It triggers **`arp-scan`** to instantly map out all active IP and MAC addresses on the local subnet.
  * For any **new** device detected, it runs a deeper **`nmap`** scan to figure out its device type and OS details (Vendor/Fingerprinting).
  * It automatically updates a local database with the live status (`Online`/`Offline`).

### 2. `setup.sh` (Automation Script)
* **What it is:** A simple Bash script for automated environment setup.
* **Why we built it:** To avoid manual, error-prone terminal commands during deployment.
* **How it works:** Once we boot up our Raspberry Pi OS, running this script will automatically update the system packages and install the required networking utilities (`nmap` and `arp-scan`) with a single command.

### 3. `schema.sql` (Database Blueprint)
* **What it is:** The structural blueprint for our local database.
* **Why we built it:** To maintain a clean, organized, and lightweight data structure.
* **How it works:** It defines the SQLite database tables (`devices`) designed to securely store device attributes (IP, MAC, Vendor, and timestamps) so the backend can easily fetch them later for our mobile app.

### 4. `.gitignore` (Security & Cleanliness)
* **What it is:** A configuration file for Git.
* **Why we built it:** To keep our GitHub repository clean and secure.
* **How it works:** It ensures that local cache files and local SQLite database files (which contain real device data) are never accidentally uploaded to the public or shared repository.

---

## How We Will Run It (Next Steps)
Once the Raspberry Pi hardware arrives, our execution steps will be:
1. Clone this repository onto the Raspberry Pi.
2. Run the automated setup script:
   ```bash
   bash setup.sh
