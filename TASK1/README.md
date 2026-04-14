# 🛡️ Network Packet Sniffer Project

## 📝 Project Overview
[cite_start]The **Python Network Packet Sniffer** is a specialized tool designed to intercept, inspect, and analyze data packets as they travel across a network interface[cite: 6]. [cite_start]Built using the **Scapy framework**, this script demonstrates how data encapsulation works within the **OSI model** by providing real-time visibility into local area network (LAN) traffic[cite: 7, 8].

---

## 🚀 Core Functionality
* [cite_start]**Packet Interception:** Captures live traffic directly from the Network Interface Card (NIC)[cite: 10].
* [cite_start]**Protocol Identification:** Automatically detects Layer 3 (IP) and Layer 4 (TCP/UDP) protocols[cite: 11].
* [cite_start]**Data Extraction:** Isolates and displays source/destination metadata and raw payload content[cite: 12].
* [cite_start]**Memory Efficiency:** Uses `store=False` to ensure the script can run for long periods without consuming system RAM[cite: 28].

---

## ⚙️ How to Run

### 1. Prerequisites
* [cite_start]**Python 3.x** installed[cite: 34].
* [cite_start]**Scapy Library:** Install via terminal using `pip install scapy`[cite: 36].
* **Drivers:** Windows users need **Npcap**; [cite_start]Linux users need **Libpcap**[cite: 37].

### 2. Execution
[cite_start]Since sniffing interacts directly with hardware, it requires **elevated privileges**[cite: 39]:
* [cite_start]**Windows:** Open PowerShell/CMD as **Administrator** and run `python TASK1.py`[cite: 40].
* [cite_start]**Linux/macOS:** Run `sudo python3 TASK1.py`[cite: 41].

---

## 📑 Project Report Summary (`TASK1_REPORT.pdf`)

### Technical Implementation
[cite_start]The project is structured into three primary logical components[cite: 15]:
1. [cite_start]**Filter Logic:** Focuses on the **Internet Protocol (IP)** layer to extract "Who" and "Where" metadata[cite: 16, 18].
2. [cite_start]**Protocol Detection:** Identifies **TCP** (connection-oriented) and **UDP** (connectionless) traffic[cite: 19, 21, 22].
3. [cite_start]**Payload Decoding:** Implements a `try-except` block to prevent crashes when encountering encrypted or binary data[cite: 26].

### Learning Outcomes
* [cite_start]**The OSI Model:** Practical experience with Layers 3 (Network) and 4 (Transport)[cite: 44].
* [cite_start]**Data Serialization:** Learning how raw bytes transform into human-readable headers[cite: 48].
* [cite_start]**Cybersecurity Ethics:** Understanding the legal boundaries of network monitoring[cite: 49].

---

## 💡 Conclusion
[cite_start]While this tool effectively categorizes traffic, it highlights the critical importance of **encryption (TLS/SSL)**, as unencrypted data is easily visible[cite: 52]. [cite_start]Future iterations could include graphical dashboards and automated threat detection[cite: 53].
