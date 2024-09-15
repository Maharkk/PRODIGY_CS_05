# Network Packet Analyzer

## Overview

The **Network Packet Analyzer** is a Python-based tool designed to capture and analyze network packets. Built using the Scapy library, this tool provides an easy-to-use interface for monitoring network traffic and examining key details such as IP addresses, protocols, and payload data. It is intended for educational purposes and must be used ethically with explicit permission on the networks being monitored.

## Features

- **Packet Capture**: Captures network packets in real-time.
- **Detailed Analysis**: Displays source and destination IP addresses, as well as packet protocols (TCP, UDP).
- **Payload Inspection**: Shows payload data for TCP and UDP packets.
- **Logging**: Saves captured packet details to a text file for later review.
- **Ethical Use**: Includes a disclaimer and consent mechanism to ensure responsible use of the tool.

## Prerequisites

Before using this tool, ensure you have the following:

- **Python**: The script requires Python 3.x.
- **Scapy Library**: Install Scapy using pip.

To install Scapy, run:

```bash
pip install scapy
```

## Installation

1. **Clone the Repository**

   Clone the repository to your local machine using Git:

   ```bash
   git clone https://github.com/Maharkk/PRODIGY_CS_05.git
   cd network-packet-analyzer
   ```

2. **Install Dependencies**

   Ensure that Scapy is installed. If not, you can install it using pip as mentioned in the prerequisites.

## Usage

1. **Run the Script**

   Execute the script from the command line:

   ```bash
   python packet_sniffer.py
   ```

2. **Follow Prompts**

   - **Disclaimer**: The script will display a disclaimer regarding the ethical use of the tool.
   - **Consent**: You must accept the terms and conditions to proceed. If you decline, the script will exit.

3. **Monitoring and Logging**

   Once you accept the terms, the tool will start capturing network packets and logging details to `packet_capture_output.txt`. You can stop the capture process by interrupting the script (e.g., by pressing `Ctrl+C`).

## Disclaimer

This tool is designed exclusively for educational and ethical purposes. Unauthorized use, distribution, or modification is strictly prohibited. By using this tool, you agree to the following:

1. **Permission**: Use this tool only on networks and systems where you have explicit permission.
2. **Legal Compliance**: Do not use this tool to breach any laws, regulations, or service agreements.
3. **Non-Harmful Use**: Avoid using this tool to harm, disrupt, or exploit networks or systems.
4. **Confidentiality**: Do not intercept, collect, or store sensitive or confidential information.
5. **Redistribution**: Do not redistribute or sell this tool without permission from the author.
6. **Responsibility**: The author is not liable for any damages or losses resulting from the use of this tool.
7. **Privacy**: Respect the privacy and security of all networks and systems accessed with this tool.



