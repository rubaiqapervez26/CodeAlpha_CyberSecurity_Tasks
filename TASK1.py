from scapy.all import sniff, IP, TCP, UDP

def process_packet(packet):
    print("\n--- Packet Captured ---")

    # Check if packet has IP layer
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")

        # Protocol detection
        if packet.haslayer(TCP):
            print("Protocol: TCP")
        elif packet.haslayer(UDP):
            print("Protocol: UDP")
        else:
            print("Protocol: Other")

        # Payload (Raw data)
        if packet.payload:
            try:
                payload = bytes(packet.payload)
                print(f"Payload: {payload[:50]}")  # Show first 50 bytes
            except:
                print("Payload: Unable to decode")

def start_sniffer():
    print("Starting Network Sniffer...")
    sniff(prn=process_packet, store=False)

if __name__ == "__main__":
    start_sniffer()