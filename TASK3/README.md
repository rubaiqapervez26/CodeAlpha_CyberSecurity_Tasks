# 🛡️ Secure Authentication & Password Management

## 📝 Project Overview
The objective of this project was to analyze a functionally operational but "Insecure" Python application to identify critical security flaws and refactor it into a **"Secure-by-Design"** version. The project demonstrates a fundamental shift from development focused on functionality to development focused on security, emphasizing cryptographic hashing and robust input validation.

---

## ⚠️ Vulnerability Analysis (The "Insecure" Version)
The initial system prioritized ease of use over safety, resulting in several high-risk vulnerabilities:

| Vulnerability | Technical Flaw | Impact |
| :--- | :--- | :--- |
| **Plaintext Storage** | Passwords stored as raw text in `users.txt`. | If the server is breached, every user's password is leaked instantly. |
| **Broken Access Control** | `view_users()` prints all credentials to the console. | Total loss of confidentiality; internal threats can steal all data. |
| **Insecure Logging** | `save_login()` writes raw passwords to a secondary log file. | Operational logs become a secondary source of leaked credentials. |
| **No Input Validation** | Results are not stripped of whitespace or checked. | Leads to database clutter or login failures due to accidental spaces. |

---

## 🚀 Key Improvements & Secure Features

### 1. Zero-Knowledge Architecture
The system moved from knowing the user's password to a "Zero Knowledge" model. Instead of direct string matching, the system now uses **Mathematical Fingerprinting**.



* **One-Way Hashing:** Using `hashlib.sha256`, the system turns a password into a fixed-length string. 
* **Irreversibility:** Because hashing is a one-way function, the original password cannot be reversed from the hash.
* **Secure Authentication:** The system hashes the login input and compares it against the stored "fingerprint" rather than comparing raw text.

### 2. Input Sanitization
* **Whitespace Removal:** Implemented `.strip()` to ensure leading/trailing spaces don't cause errors.
* **Null-Check Logic:** Prevents the creation of empty accounts.

---

## 📊 Feature Comparison Table

| Feature | Vulnerable Code (`VULNERABLE CODE.py`) | Secure Code (`SECURE CODE.py`) |
| :--- | :--- | :--- |
| **Password Format** | Raw text | Hashed hex string (SHA-256) |
| **External Logging** | Saves to `log.txt` (Critical Risk) | No insecure logging |
| **User Privacy** | `view_users()` reveals all credentials | Function removed/obfuscated |
| **Input Cleaning** | None | `.strip()` implemented |
| **Primary Library** | `os` | `hashlib` |

---

## 🛠️ Future Recommendations
To reach production-ready standards, the following enhancements are recommended:
* **Sal
