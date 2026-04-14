# 🛡️ Cybersecurity Internship Portfolio (CodeAlpha)

## 👤 Intern Information
* **Intern Name:** Rubaiqa Pervez
* **Student ID:** CA/DF1/42124
* **Organization:** CodeAlpha
* **Role:** Cyber Security Intern
* **Duration:** April 1, 2026 – April 30, 2026

---

## 📂 Project Overview
This repository documents the completion of three core cybersecurity tasks, transitioning from offensive network monitoring to defensive software engineering and organizational security training.

| Task | Title | Description | Key Tech |
| :--- | :--- | :--- | :--- |
| **Task 1** | [Network Packet Sniffer](#-task-1-network-packet-sniffer) | Real-time traffic analysis and protocol detection. | Python, Scapy |
| **Task 2** | [Phishing Awareness](#-task-2-phishing-awareness-training) | Educational security training modules. | PPTX, Security Audit |
| **Task 3** | [Secure Authentication](#-task-3-secure-authentication-system) | Refactoring code for cryptographic safety. | Python, Hashlib |

---

## 📡 Task 1: Network Packet Sniffer

### Overview
A specialized tool built to intercept and analyze data packets across a network interface. It provides visibility into the "conversations" happening between devices on a LAN, focusing on Layers 3 (Network) and 4 (Transport) of the OSI model.

### Technical Implementation
* **Filter Logic:** Utilizes `if packet.haslayer(IP):` to bypass network noise (ARP/Ethernet) and focus on IP traffic.
* **Protocol Identification:** Automates detection of TCP (connection-oriented) and UDP (connectionless) protocols.
* **Payload Inspection:** Decodes raw bytes to preview the first 50 bytes of data for Deep Packet Inspection (DPI).
* **Operational Efficiency:** Uses `store=False` in the sniff function to prevent memory exhaustion during long-term monitoring.

---

## 🎣 Task 2: Phishing Awareness Training

### Overview
An educational module designed to reduce human-error risk—the leading cause of 90% of data breaches. This project focuses on identifying the psychological and technical markers of social engineering.

### Core Modules
* **Social Engineering Tactics:** Analysis of how attackers use **Urgency**, **Fear**, and **Authority** to manipulate user behavior.
* **Attack Vectors:** Comprehensive guides on **Smishing** (SMS), **Vishing** (Voice), and **Spear Phishing** (Targeted).
* **Technical Red Flags:** Training on spotting mismatched URLs (e.g., `http://bank-login123.com`) and verifying SSL/TLS certificates (HTTPS).
* **Mitigation:** Promoting the use of **Multi-Factor Authentication (MFA)** and secure network protocols.

---

## 🔒 Task 3: Secure Authentication System

### Overview
A security audit and refactor project that transformed a "Vulnerable" application into a "Secure-by-Design" system. This demonstrates the transition from plaintext storage to cryptographic security.

### Security Improvements & Mitigation
* **Cryptographic Hashing:** Replaced `users.txt` plaintext storage with **SHA-256 Hashing**. 
* **Zero-Knowledge Architecture:** The system validates users via mathematical fingerprints; even if the database is breached, passwords remain unreadable.
* **Input Sanitization:** Implemented `.strip()` and null-check logic to prevent **Credential Stuffing** errors and accidental login failures.
* **Access Control:** Removed insecure administrative functions like `view_users()` that previously exposed all credentials to the console.

---

## 🎓 Skills Demonstrated
* **Traffic Analysis:** Proficient in network buffer interaction and protocol analysis.
* **Defensive Development:** Expert in implementing one-way hashing and secure file handling.
* **Risk Assessment:** Identifying vulnerabilities in both software logic and human behavior.
* **Ethical Standards:** Understanding the legal boundaries and responsibilities of monitoring network traffic.

---

### 🚀 Setup and Usage
To run the Python tools, ensure you have the necessary libraries:
```bash
pip install scapy
