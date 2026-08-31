"""
Sprint 2 - Signature-Based Threat Detection

Preliminary Proof of Concept

Suricata performs the actual signature-based threat detection.

This script demonstrates how Suricata EVE JSON alert events can be
read and converted into a simplified structured security-event format
for later integration with the Assas backend and storage components.

This is not the final implementation.
"""

import json


# Default Suricata EVE JSON location.
# The actual path will be verified during deployment.
EVE_FILE = "/var/log/suricata/eve.json"


def parse_alert(event):
    """
    Convert a Suricata alert event into the simplified
    security-event structure required by the project.
    """

    alert = event.get("alert", {})

    return {
        "timestamp": event.get("timestamp"),
        "source_ip": event.get("src_ip"),
        "destination_ip": event.get("dest_ip"),
        "source_port": event.get("src_port"),
        "destination_port": event.get("dest_port"),
        "protocol": event.get("proto"),
        "signature": alert.get("signature"),
        "category": alert.get("category"),
        "severity": alert.get("severity")
    }


def read_suricata_alerts():
    """
    Read Suricata EVE JSON events and process alert events.
    """

    try:
        with open(EVE_FILE, "r") as file:

            for line in file:
                try:
                    event = json.loads(line)

                    if event.get("event_type") == "alert":
                        security_event = parse_alert(event)

                        print(
                            json.dumps(
                                security_event,
                                indent=4
                            )
                        )

                except json.JSONDecodeError:
                    print("Skipped invalid JSON event.")

    except FileNotFoundError:
        print(
            "Suricata eve.json was not found. "
            "Verify that Suricata is installed, running, "
            "and configured to generate EVE JSON output."
        )


if __name__ == "__main__":
    read_suricata_alerts()
