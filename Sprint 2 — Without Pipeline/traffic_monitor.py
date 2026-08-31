"""
Sprint 2 - Real-Time Network Monitoring

Preliminary Proof of Concept

This script demonstrates continuous programmatic monitoring of live
network traffic and extraction of selected basic packet information.

Traffic processing is treated as an internal implementation step of
Real-Time Network Monitoring rather than as a separate product feature.

This is not the final implementation and will be validated and refined
on the Raspberry Pi environment.
"""

from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime


# Example network interface.
# The actual monitoring interface will be identified
# during Raspberry Pi configuration.
INTERFACE = "eth0"


def process_packet(packet):
    """
    Extract selected monitoring information from each IP packet.
    """

    if IP not in packet:
        return

    monitoring_data = {
        "timestamp": datetime.now().isoformat(),
        "source_ip": packet[IP].src,
        "destination_ip": packet[IP].dst,
        "protocol": packet[IP].proto,
        "packet_size": len(packet)
    }

    if TCP in packet:
        monitoring_data["protocol"] = "TCP"
        monitoring_data["source_port"] = packet[TCP].sport
        monitoring_data["destination_port"] = packet[TCP].dport

    elif UDP in packet:
        monitoring_data["protocol"] = "UDP"
        monitoring_data["source_port"] = packet[UDP].sport
        monitoring_data["destination_port"] = packet[UDP].dport

    print(monitoring_data)


def start_monitoring():
    """
    Start continuous monitoring on the selected network interface.
    """

    print(f"Starting real-time network monitoring on {INTERFACE}...")
    print("Press Ctrl+C to stop.")

    sniff(
        iface=INTERFACE,
        prn=process_packet,
        store=False
    )


if __name__ == "__main__":
    start_monitoring()
