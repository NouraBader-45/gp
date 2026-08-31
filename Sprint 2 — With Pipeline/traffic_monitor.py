
"""
Sprint 2 - Real-Time Traffic Monitoring Pipeline

Preliminary Proof of Concept

This script demonstrates programmatic live packet capture as an
initial feasibility check for the Real-Time Traffic Monitoring Pipeline.

It is not the final flow-processing implementation.
CICFlowMeter and NFStream will be evaluated before selecting the
final approach for extracting flow-level statistics.
"""

from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime


# Example network interface.
# This will be changed to the actual monitoring interface
# during Raspberry Pi configuration.
INTERFACE = "eth0"


def process_packet(packet):
    """
    Extract and display basic information from each captured IP packet.
    """

    if IP not in packet:
        return

    packet_info = {
        "timestamp": datetime.now().isoformat(),
        "source_ip": packet[IP].src,
        "destination_ip": packet[IP].dst,
        "protocol": packet[IP].proto,
        "packet_size": len(packet)
    }

    if TCP in packet:
        packet_info["protocol"] = "TCP"
        packet_info["source_port"] = packet[TCP].sport
        packet_info["destination_port"] = packet[TCP].dport

    elif UDP in packet:
        packet_info["protocol"] = "UDP"
        packet_info["source_port"] = packet[UDP].sport
        packet_info["destination_port"] = packet[UDP].dport

    print(packet_info)


def start_monitoring():
    """
    Start continuous packet capture on the selected interface.
    """

    print(f"Starting real-time traffic monitoring on {INTERFACE}...")
    print("Press Ctrl+C to stop.")

    sniff(
        iface=INTERFACE,
        prn=process_packet,
        store=False
    )


if __name__ == "__main__":
    start_monitoring()
