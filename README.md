# Multi-Threaded Port Scanner with Banner Grabbing

A multi-threaded Python-based port scanner that quickly scans a range of ports, identifies open ports, and grabs available service banners. This is a common reconnaissance tool used in cybersecurity and penetration testing.

---

## 🚀 Features
- 🔍 Scans ports 1–1024 by default (easily adjustable).
- ⚡ Multi-threaded for high-performance scanning.
- 📄 Captures and displays service banners when available.
- 🎯 Target host is customizable within the script.

---

## 🛠️ Usage

### 1️⃣ Install Dependencies
This script uses only built-in Python libraries (`socket`, `threading`, `queue`), so no external installations are required.

### 2️⃣ Edit the Target Host
Edit the `target_host` variable in `port_scanner.py`:
```python
target_host = 'scanme.nmap.org'
```

### 3️⃣ Run the Scanner
```bash
Python3 port-scanner.py
```

### 📑 OUTPUT example

```kotlin
[+] Port 22 is open | Banner: SSH-2.0-OpenSSH_7.4
[+] Port 80 is open | Banner: HTTP/1.1 200 OK
Scan complete!
```
