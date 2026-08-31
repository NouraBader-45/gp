# Sprint 2 – Real-Time Network Monitoring and Signature-Based Threat Detection

## 1. Sprint Overview

Sprint 2 focuses on providing continuous visibility into local network activity and detecting known security threats.

The sprint consists of two main features:

1. Real-Time Network Monitoring
2. Signature-Based Threat Detection

Real-Time Network Monitoring continuously observes mirrored local network traffic and produces the traffic information required by other system components.

Signature-Based Threat Detection integrates Suricata IDS to detect known or rule-matching malicious and suspicious network activities.

Traffic capture, processing, and statistics extraction will remain part of the technical implementation of Real-Time Network Monitoring but will not be treated as a separate product feature.

---

## 2. Sprint Features

### 2.1 Real-Time Network Monitoring

The Real-Time Network Monitoring feature continuously monitors mirrored local network traffic to provide visibility into network activity.

The feature may extract selected information such as:

- Source and destination addresses
- Network protocol
- Packet counts
- Traffic volume
- Packet rate
- Flow duration
- Timestamp

The exact monitoring information will be finalized after validating the selected implementation approach.

### 2.2 Signature-Based Threat Detection

The Signature-Based Threat Detection feature integrates Suricata IDS to analyze monitored traffic using established security rules and signatures.

The prototype will validate a selected set of known or rule-matching security activities supported by the configured Suricata rules.

---

## 3. System Flow

The general system flow is:

Local Network Devices
        ↓
Managed Switch
        ↓
Port Mirroring
        ↓
Raspberry Pi
        ↓
Real-Time Network Monitoring
        ↓
Traffic Processing
        ↓
Traffic Information / Statistics
        ↓
Backend / Storage

The same monitored traffic will also be analyzed through:

Mirrored Network Traffic
        ↓
Suricata IDS
        ↓
Signature / Rule Matching
        ↓
Security Alert
        ↓
Structured Security Event
        ↓
Backend / Storage

Traffic processing is therefore an internal implementation step of Real-Time Network Monitoring rather than a separate product feature.

---

## 4. Implementation Approach

### 4.1 Network Environment Setup

The implementation will begin with the network-monitoring environment.

The following steps will be performed:

1. Prepare Raspberry Pi OS.
2. Connect the Raspberry Pi to the managed switch.
3. Configure port mirroring on the managed switch.
4. Select the Raspberry Pi interface that receives mirrored traffic.
5. Verify that the expected network traffic reaches the Raspberry Pi.
6. Validate the configuration using tcpdump or Wireshark.

### 4.2 Real-Time Network Monitoring

After validating the network environment, the system will:

1. Receive live mirrored network traffic.
2. Continuously observe network activity.
3. Process the received traffic using existing traffic-processing tools.
4. Extract the monitoring information required by the system.
5. Convert the required information into a structured format.
6. Make the resulting monitoring information available to backend and user-interface components.

The project will not implement low-level packet-capture functionality from scratch.

### 4.3 Suricata IDS Integration

The signature-based detection component will be implemented by:

1. Installing Suricata on the Raspberry Pi.
2. Configuring the monitored network interface.
3. Configuring and enabling the selected Suricata rules.
4. Verifying successful rule loading.
5. Confirming that Suricata receives the mirrored traffic.
6. Running selected controlled test scenarios.
7. Confirming generation of expected security alerts.
8. Extracting the relevant alert fields.
9. Converting generated alerts into the project's structured security-event format.
10. Making the security-event information available to later components.

---

## 5. Build vs. Existing Technology Decision

### Real-Time Network Monitoring

Existing packet-capture and traffic-processing technologies will be used for low-level network monitoring.

The project's implementation work will focus on:

- Network configuration
- Continuous monitoring
- Selection of required traffic information
- Traffic processing
- Structured output generation
- Integration with other system components

Traffic processing is considered an internal technical step rather than an independent project feature.

### Signature-Based Threat Detection

Suricata will provide the existing signature-based intrusion-detection engine.

The project will focus on:

- Suricata installation
- Configuration
- Rule management
- Traffic integration
- Alert extraction
- Alert processing
- Security-event formatting
- System integration

---

## 6. Dataset, Model, and API Decisions

| Feature | Training Dataset | ML Model | Model Training | External API | Existing Technology |
|---|---|---|---|---|---|
| Real-Time Network Monitoring | Not required | None | Not required | None | Network capture/processing tools |
| Signature-Based Threat Detection | Not required | None | Not required | None | Suricata IDS |

### Dataset Decision

No training dataset is required for Sprint 2.

Live mirrored network traffic is the main operational data source.

Sample PCAP files may be used for controlled and reproducible testing.

### Model Decision

No machine-learning model is required for either Sprint 2 feature.

Machine-learning anomaly detection is handled separately by another project feature.

### External API Decision

No external cloud API is required for the core Sprint 2 functionality.

Monitoring and Suricata-based detection operate locally.

---

## 7. Inputs and Outputs

### Real-Time Network Monitoring

#### Input

- Live mirrored network traffic
- Network packets received by the Raspberry Pi
- Optional PCAP files for controlled testing

#### Output

The monitoring component will produce selected structured network information, which may include:

- Source and destination addresses
- Protocol information
- Packet counts
- Traffic volume
- Packet rate
- Flow duration
- Timestamp

The final output schema will be determined after implementation validation.

### Signature-Based Threat Detection

#### Input

- Mirrored network traffic
- Configured Suricata security rules
- Controlled test traffic or PCAP files during validation

#### Output

The resulting security-event information may include:

- Timestamp
- Source IP
- Destination IP
- Detection signature
- Alert category
- Severity

---

## 8. Tools and Technologies

The initial technologies considered for Sprint 2 are:

- Raspberry Pi 5
- Raspberry Pi OS / Linux
- Managed Switch with Port Mirroring
- Suricata IDS
- tcpdump
- Wireshark
- Python
- Traffic-processing tools selected during implementation validation
- Git and GitHub

CICFlowMeter may be evaluated for flow-level processing if detailed flow statistics are required by later system components.

---

## 9. Planned Implementation Structure

A possible source-code structure is:

edge/
└── monitoring/
    ├── capture/
    ├── processing/
    ├── suricata/
    └── tests/

The exact source files will be created after the implementation approach is validated.

Sprint documentation will remain under:

docs/
└── sprint-2/
    └── README.md

---

## 10. Testing Plan

### Real-Time Monitoring Tests

The monitoring component will be tested by:

1. Confirming that mirrored traffic reaches the Raspberry Pi.
2. Comparing monitored traffic with tcpdump or Wireshark.
3. Confirming continuous monitoring.
4. Validating the selected monitoring information.
5. Testing with live network traffic.
6. Using controlled PCAP inputs when reproducible testing is required.

### Suricata Tests

Suricata integration will be tested by:

1. Verifying successful Suricata installation.
2. Verifying successful rule loading.
3. Confirming that Suricata receives monitored traffic.
4. Running selected controlled security scenarios.
5. Confirming that expected alerts are generated.
6. Validating the required alert fields.
7. Confirming successful conversion into structured security events.

### Performance Checks

The prototype will monitor:

- CPU utilization
- Memory utilization
- Monitoring stability
- Processing delays under continuous traffic

---

## 11. Acceptance Criteria

Sprint 2 will be considered complete when:

1. Mirrored local network traffic can be continuously observed by the Raspberry Pi.
2. The system can produce the selected network-monitoring information.
3. Suricata successfully receives and analyzes monitored traffic.
4. Selected controlled security scenarios generate expected Suricata alerts.
5. Relevant alerts are converted into structured security events.
6. Monitoring and signature-based detection operate locally.
7. Monitoring and security-event information can be consumed by later backend components.

---

## 12. Manageability

Sprint 2 is considered manageable because the project relies on existing technologies for low-level traffic monitoring and signature-based intrusion detection.

The project does not implement a packet-capture engine or IDS engine from scratch.

The main implementation work is limited to network configuration, monitoring integration, traffic processing, Suricata configuration, alert processing, structured data generation, and testing.

The scope will also be limited to the network information required by the project and a representative set of security test scenarios.

---

## 13. Dependencies

Sprint 2 depends on:

- Raspberry Pi hardware
- Raspberry Pi OS
- Managed switch with port-mirroring support
- Correct test-network configuration
- Network-monitoring tools
- Suricata IDS
- Compatible Suricata rules
- Controlled security-testing environment

---

## 14. Risks and Limitations

The main limitations are:

- Encrypted traffic limits visibility into application payloads.
- Signature-based detection depends on configured rules and known signatures.
- Port-mirroring misconfiguration may result in incomplete traffic visibility.
- Raspberry Pi performance may be affected by high traffic volumes.
- Monitoring information available to the system depends on the selected processing tools.
- The system performs passive monitoring and does not directly block network traffic.
- The prototype will validate representative security scenarios rather than every possible attack.

---

## 15. References

The implementation will rely on approved project references, including:

- Suricata official resources and documentation
- Raspberry Pi OS documentation
- tcpdump resources
- CICFlowMeter resources if flow-level extraction is required
- Relevant networking and cybersecurity references listed in the project proposal
