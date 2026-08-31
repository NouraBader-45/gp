import subprocess
import sqlite3
import re
from datetime import datetime


def setup_database():
    conn = sqlite3.connect('rasidnet_inventory.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS devices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip_address TEXT UNIQUE,
            mac_address TEXT,
            vendor TEXT,
            os_details TEXT,
            first_seen TIMESTAMP,
            last_seen TIMESTAMP,
            status TEXT
        )
    ''')
    conn.commit()
    return conn


def run_arp_scan(interface="eth0"):
    print(f"[*] Starting fast ARP scan on {interface}...")
    devices = []
    try:
        result = subprocess.check_output(['sudo', 'arp-scan', '--interface', interface, '--localnet'], text=True)
        
        for line in result.split('\n'):
            match = re.search(r'(\d+\.\d+\.\d+\.\d+)\s+([0-9a-fA-F:]+)\s+(.*)', line)
            if match:
                ip = match.group(1)
                mac = match.group(2)
                vendor = match.group(3)
                devices.append({'ip': ip, 'mac': mac, 'vendor': vendor})
    except Exception as e:
        print(f"[!] Error running arp-scan: {e}")
    
    return devices


def run_nmap_os_scan(ip):
    print(f"    -> Running deep Nmap scan on {ip}...")
    try:
        result = subprocess.check_output(['sudo', 'nmap', '-O', '-F', ip], text=True)
        if "Running:" in result:
            os_line = [line for line in result.split('\n') if "Running:" in line][0]
            return os_line.replace("Running: ", "")
    except Exception:
        pass
    return "Unknown OS"

def update_inventory(conn, active_devices):
    cursor = conn.cursor()
    current_time = datetime.now()

    cursor.execute("UPDATE devices SET status = 'Offline'")

    for dev in active_devices:
        ip = dev['ip']
        mac = dev['mac']
        vendor = dev['vendor']
        
        cursor.execute("SELECT * FROM devices WHERE mac_address = ?", (mac,))
        row = cursor.fetchone()

        if row is None:
            os_details = run_nmap_os_scan(ip)
            cursor.execute('''
                INSERT INTO devices (ip_address, mac_address, vendor, os_details, first_seen, last_seen, status)
                VALUES (?, ?, ?, ?, ?, ?, 'Online')
            ''', (ip, mac, vendor, os_details, current_time, current_time))
            print(f"[+] NEW Device Found! IP: {ip} | Vendor: {vendor}")
        else:
            cursor.execute('''
                UPDATE devices
                SET last_seen = ?, status = 'Online', ip_address = ?
                WHERE mac_address = ?
            ''', (current_time, ip, mac))
            print(f"[*] Updated Device Status: {ip} is still Online.")

    conn.commit()


if __name__ == "__main__":
    print("=== Yaqith/RasidNet Network Discovery Started ===")
    
    # 1. تجهيز قاعدة البيانات
    db_conn = setup_database()
    
    discovered_devices = run_arp_scan(interface="eth0")
    
    if discovered_devices:
        print(f"\n[✓] Found {len(discovered_devices)} active devices. Updating Database...")
        update_inventory(db_conn, discovered_devices)
    else:
        print("[-] No active devices found on the network.")
        
    db_conn.close()
    print("=== Discovery Cycle Completed ===")
