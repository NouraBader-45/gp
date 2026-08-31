# Sprint 2 – Real-Time Traffic Monitoring Pipeline and Signature-Based Threat Detection

## 1. Sprint Overview

Sprint 2 focuses on continuously monitoring local network traffic and detecting known security threats.

The sprint consists of two main features:

1. Real-Time Traffic Monitoring Pipeline
2. Signature-Based Threat Detection

The monitoring pipeline receives mirrored network traffic, processes it, and extracts relevant traffic and flow-level statistics. In parallel, Suricata IDS analyzes the monitored traffic using predefined security rules and signatures to identify known malicious or suspicious network activity.

The outputs of this sprint will later be used by other system components, including the backend, alert-management features, and the security dashboard.

---

## 2. Sprint Features

### 2.1 Real-Time Traffic Monitoring Pipeline

The Real-Time Traffic Monitoring Pipeline continuously receives mirrored network traffic and processes it to generate structured traffic and flow-level information.

The feature will provide network information such as:

- Source IP address
- Destination IP address
- Source port
- Destination port
- Network protocol
- Packet count
- Byte count
- Packet rate
- Flow duration
- Timestamp

The exact set of extracted statistics will be finalized after validating the selected traffic-processing approach on the Raspberry Pi.

### 2.2 Signature-Based Threat Detection

The Signature-Based Threat Detection feature integrates Suricata IDS to analyze monitored network traffic using established security rules and signatures.

The feature is intended to detect selected known or rule-matching security activities, such as:

- Known malicious communication patterns
- Port scanning activity
- Selected denial-of-service patterns
- Other suspicious network activity supported by the configured Suricata rules

The system will use Suricata as an existing intrusion-detection engine rather than developing a custom signature-based IDS from scratch.

---

## 3. System Flow

The monitored network traffic will follow the following general flow:

```text
Local Network Devices
        ↓
Managed Switch
        ↓
Port Mirroring
        ↓
Raspberry Pi
        ↓
Real-Time Traffic Monitoring Pipeline
        ↓
Traffic / Flow Statistics
        ↓
Backend / Storage
```

The same mirrored traffic will also be analyzed by Suricata:

```text
Mirrored Network Traffic
        ↓
Suricata IDS
        ↓
Signature and Rule Matching
        ↓
Security Alert
        ↓
Structured Security Event
        ↓
Backend / Storage
```

The Raspberry Pi receives a copy of selected network traffic through port mirroring. It is not required to operate as an inline gateway for the monitored devices.

---

## 4. Implementation Approach

### 4.1 Network Environment Setup

The implementation will begin by preparing the network-monitoring environment.

The following steps will be performed:

1. Prepare Raspberry Pi OS.
2. Connect the Raspberry Pi to the managed switch.
3. Configure the managed switch for port mirroring.
4. Select the Raspberry Pi network interface that will receive mirrored traffic.
5. Verify that mirrored traffic reaches the Raspberry Pi.
6. Use tools such as tcpdump or Wireshark to verify that the expected traffic is visible.

### 4.2 Real-Time Traffic Monitoring Pipeline

After confirming that mirrored traffic reaches the Raspberry Pi, the monitoring pipeline will be implemented.

The implementation steps are:

1. Capture or receive live mirrored network traffic.
2. Process captured packets into meaningful traffic or flow information.
3. Extract the required statistical features.
4. Convert the extracted information into a structured format.
5. Validate the extracted information against known test traffic.
6. Make the structured monitoring data available to later system components.

An existing packet-capture or flow-processing tool will be used for low-level traffic processing instead of implementing a packet-capture engine from scratch.

CICFlowMeter or NFStream will be evaluated for flow-level traffic processing, and the final tool will be selected based on compatibility and performance on the Raspberry Pi environment.

A preliminary Python implementation is included in `traffic_monitor.py` to demonstrate that live network traffic can be captured and basic packet information can be processed programmatically before the final flow-processing tool is selected.

### 4.3 Suricata IDS Integration

The signature-based detection component will be implemented using Suricata IDS.

The implementation steps are:

1. Install Suricata on the Raspberry Pi.
2. Configure Suricata to monitor the appropriate network interface.
3. Configure and enable the required Suricata rules.
4. Verify successful rule loading.
5. Verify that Suricata receives the mirrored traffic.
6. Generate controlled test traffic.
7. Confirm that matching security activity generates Suricata alerts.
8. Extract the relevant fields from generated alerts.
9. Convert the alerts into the project's internal structured security-event format.
10. Make the resulting security events available to the backend and later system components.

A preliminary alert parser is included in `suricata_alert_parser.py` to demonstrate how Suricata EVE JSON alerts can be converted into structured security-event data.

---

## 5. Build vs. Existing Technology Decision

### Real-Time Traffic Monitoring Pipeline

The project will not develop low-level packet-capture functionality from scratch.

Existing network-capture and flow-processing tools will be used to obtain network traffic and flow information.

The project-specific implementation will focus on:

- Configuring traffic capture
- Selecting required traffic features
- Processing traffic information
- Structuring monitoring results
- Integrating the output with the rest of the system

### Signature-Based Threat Detection

Suricata is an existing IDS and will provide the signature-based detection engine.

The project will not develop a new signature-detection engine.

The project-specific implementation will focus on:

- Suricata installation
- Suricata configuration
- Rule configuration and management
- Network-interface integration
- Alert extraction
- Alert parsing
- Security-event formatting
- Integration with backend components

---

## 6. Dataset, Model, and API Decisions

| Feature | Training Dataset | ML Model | Model Training | External API | Existing Technology |
|---|---|---|---|---|---|
| Real-Time Traffic Monitoring Pipeline | Not required | None | Not required | None | Packet/flow-processing tools |
| Signature-Based Threat Detection | Not required | None | Not required | None | Suricata IDS |

### Dataset Decision

A training dataset is not required for either Sprint 2 feature because neither feature performs machine-learning model training.

Live mirrored network traffic will be the operational input.

Sample PCAP files may be used as controlled and reproducible test inputs during development and validation.

### Model Decision

Sprint 2 does not require a machine-learning model.

Machine-learning-based anomaly detection belongs to a later project feature and is outside the implementation scope of this sprint.

### External API Decision

No external cloud API is required for the core functionality of Sprint 2.

Traffic monitoring and Suricata-based detection will operate locally on the Raspberry Pi.

---

## 7. Inputs and Outputs

### 7.1 Real-Time Traffic Monitoring Pipeline

#### Input

- Live mirrored network traffic
- Packets received by the Raspberry Pi monitoring interface
- Sample PCAP files for controlled testing when required

#### Output

Structured traffic information may include:

- Source and destination addresses
- Source and destination ports
- Protocol information
- Packet counts
- Byte counts
- Packet rate
- Flow duration
- Timestamp

Example conceptual output:

```json
{
  "timestamp": "YYYY-MM-DDTHH:MM:SS",
  "source_ip": "192.168.1.10",
  "destination_ip": "8.8.8.8",
  "protocol": "UDP",
  "packet_count": 25,
  "byte_count": 5400,
  "flow_duration": 3.4,
  "packet_rate": 7.35
}
```

The final schema will be finalized during implementation.

### 7.2 Signature-Based Threat Detection

#### Input

- Live mirrored network traffic
- Configured Suricata rules and signatures
- Controlled PCAP or test-network traffic during validation

#### Output

Relevant security-event information may include:

- Timestamp
- Source IP
- Destination IP
- Detection signature
- Alert category
- Severity

Example conceptual output:

```json
{
  "timestamp": "YYYY-MM-DDTHH:MM:SS",
  "source_ip": "192.168.1.10",
  "destination_ip": "192.168.1.20",
  "signature": "Example Suricata Signature",
  "category": "Example Category",
  "severity": 2
}
```

---

## 8. Tools and Technologies

The initial technologies considered for Sprint 2 are:

- Raspberry Pi 5 – local edge monitoring and processing
- Raspberry Pi OS / Linux – operating environment
- Managed Switch with Port Mirroring – traffic duplication
- Suricata IDS – signature-based threat detection
- tcpdump – command-line packet capture and verification
- Wireshark – traffic inspection and troubleshooting
- CICFlowMeter / NFStream – candidate tools to be evaluated for flow-level traffic processing
- Scapy – preliminary programmatic packet-capture implementation
- Python – traffic-processing and integration scripts
- Git and GitHub – version control and technical documentation

---

## 9. Preliminary Implementation Files

Preliminary implementation files are included alongside this README to demonstrate the technical feasibility of the proposed approach and to provide a starting reference for later development.

These files are not considered the final Sprint 2 implementation and will be validated and refined during development on the Raspberry Pi environment.

### `traffic_monitor.py`

Provides a preliminary proof of concept for:

- Capturing live packets from a network interface
- Reading basic packet information
- Demonstrating programmatic real-time traffic monitoring

The final flow-level processing will be implemented after CICFlowMeter and NFStream are evaluated.

### `suricata_alert_parser.py`

Provides a preliminary proof of concept for:

- Reading Suricata EVE JSON output
- Identifying Suricata alert events
- Extracting relevant alert information
- Converting alerts into a simplified structured security-event format

### `requirements.txt`

Lists the Python dependencies required by the current preliminary implementation.

---

## 10. Implementation Structure

The current Sprint 2 structure is:

```text
sprint2/
└── traffic_monitoring_and_ids/
    ├── README.md
    ├── traffic_monitor.py
    ├── suricata_alert_parser.py
    └── requirements.txt
```

The structure may be expanded during development after the final flow-processing approach is selected and the components are validated on the Raspberry Pi.

---

## 11. Testing Plan

### Network Monitoring Tests

The monitoring feature will be tested by:

1. Confirming that mirrored traffic reaches the Raspberry Pi.
2. Comparing observed traffic with tcpdump or Wireshark.
3. Verifying continuous traffic processing.
4. Validating extracted traffic information.
5. Testing with live network traffic.
6. Testing with controlled PCAP files when required.

### Suricata Tests

The Suricata component will be tested by:

1. Verifying successful Suricata installation.
2. Verifying successful rule loading.
3. Confirming that Suricata receives the monitored traffic.
4. Generating selected controlled security scenarios.
5. Confirming that matching rules generate alerts.
6. Validating the required alert fields.
7. Verifying successful conversion of Suricata alerts into structured security events.

### Performance Tests

The prototype will also monitor:

- Raspberry Pi CPU utilization
- Memory utilization
- Processing stability during continuous monitoring
- Potential traffic-processing delays

---

## 12. Acceptance Criteria

Sprint 2 will be considered complete when:

1. Mirrored network traffic is successfully received by the Raspberry Pi.
2. Live traffic can be continuously monitored.
3. The selected traffic statistics can be extracted in a structured format.
4. Suricata successfully analyzes the monitored traffic.
5. Selected controlled security scenarios generate valid Suricata alerts.
6. Relevant alert fields can be converted into structured security events.
7. Monitoring and signature-based detection operate locally without requiring an external cloud service.
8. The resulting monitoring and security data can be consumed by later system components.

---

## 13. Manageability

Sprint 2 is considered technically manageable because the project does not implement low-level packet-capture technology or a signature-based intrusion-detection engine from scratch.

Existing technologies will provide the low-level traffic-capture and signature-detection capabilities, while the project's implementation will focus on configuration, traffic processing, structured data generation, integration, and testing.

To keep the prototype scope manageable, the implementation will focus on a defined set of traffic statistics and representative security test scenarios rather than attempting to detect every possible network attack.

The included preliminary implementation files provide an initial proof of concept for packet capture and Suricata alert processing. Full validation will be performed in the target Raspberry Pi environment.

---

## 14. Dependencies

Sprint 2 depends on:

- Raspberry Pi hardware
- Raspberry Pi OS
- Managed switch with port-mirroring support
- Correct port-mirroring configuration
- Selected traffic-processing tool
- Suricata installation
- Compatible Suricata rules
- Python and required Python libraries
- Controlled network-testing environment

---

## 15. Risks and Limitations

The main limitations include:

- Encrypted network traffic limits visibility into application payloads.
- Signature-based detection is limited to known or rule-matching security activity.
- Incorrect port-mirroring configuration may cause incomplete traffic visibility.
- High network traffic volume may affect Raspberry Pi performance.
- Available flow-level features may depend on the selected processing tool.
- CICFlowMeter and NFStream require practical evaluation before selecting the final flow-processing approach.
- The prototype performs passive monitoring and detection and does not directly block network traffic.
- The prototype will validate selected representative security scenarios rather than every possible threat.

---

## 16. References

The implementation will rely on the project's approved technical references, including:

- Suricata official resources and documentation
- Raspberry Pi OS documentation
- CICFlowMeter resources
- NFStream resources
- tcpdump documentation
- Scapy documentation
- Relevant network-monitoring and cybersecurity references listed in the project proposal
