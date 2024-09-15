import sys
from scapy.all import sniff, IP, TCP, UDP

# Set the path and filename for the output text file
OUTPUT_FILE = 'packet_capture_output.txt'

def display_disclaimer():
    print("------------------------ Packet Sniffer Tool Disclaimer ---------------------------")
    print("This packet sniffer tool is designed for educational and ethical use only.")
    print("Unauthorized use, distribution, or modification of this tool is strictly prohibited.")
    print("By using this tool, you agree to the following terms and conditions:")
    print("\n1. You will use this tool only on networks and systems for which you have explicit permission.")
    print("2. You will not use this tool to breach any laws, regulations, or terms of service agreements.")
    print("3. You will refrain from using this tool to harm, disrupt, or exploit networks or systems.")
    print("4. You will not use this tool to intercept, collect, or store sensitive or confidential information.")
    print("5. You will not redistribute or sell this tool without obtaining express permission from the author.")
    print("6. The author accepts no responsibility for any damages or losses resulting from the use of this tool.")
    print("7. You will respect the privacy and security of all networks and systems you access with this tool.")
    print("-------------------------------------------------------------------------------------")

def get_user_consent():
    accept_terms = input("\nDo you accept these terms and conditions? (y/n): ")
    if accept_terms.lower() != 'y':
        print("You must accept the terms and conditions to use this tool.")
        sys.exit()

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        # Prepare packet information to be written to file
        packet_info = f"Source IP: {ip_src}\nDestination IP: {ip_dst}\nProtocol: {protocol}\n"

        # Add TCP or UDP payload data if present
        if TCP in packet:
            packet_info += f"TCP Payload: {packet[TCP].payload}\n"
        elif UDP in packet:
            packet_info += f"UDP Payload: {packet[UDP].payload}\n"

        packet_info += "-----\n"

        # Write packet information to file
        with open(OUTPUT_FILE, 'a') as file:
            file.write(packet_info)

        # Print packet information to console (optional)
        print(packet_info)

def start_sniffing():
    print("Starting packet capture...")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    display_disclaimer()
    get_user_consent()
    start_sniffing()
